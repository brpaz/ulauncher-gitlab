"""Ulauncher extension main class"""

import logging
import gitlab
import re
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, PreferencesEvent, PreferencesUpdateEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction

LOGGER = logging.getLogger(__name__)

PROJECTS_SEARCH_TYPE_PUBLIC = 'PUBLIC'
PROJECTS_SEARCH_TYPE_MEMBER = 'MEMBER'
PROJECTS_SEARCH_TYPE_STARRED = 'STARRED'


class GitLabExtension(Extension):
    """ Main extension class """

    def __init__(self):
        """ init method """
        LOGGER.info('Initializing GitLab Extension')
        super(GitLabExtension, self).__init__()

        # initializes GitLab Client
        self.gitlab = None
        self.current_user = None

        # Event listeners
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def show_menu(self):
        """ Show the main extension menu, when the user types the extension keyword without arguments """
        keyword = self.preferences["kw"]

        menu = [
            ExtensionResultItem(icon='images/icon.png',
                                name="My",
                                description="Your personal menu with shortcuts for your Issues, Merge Requests and more",
                                highlightable=False,
                                on_enter=SetUserQueryAction("%s my" % keyword)),
            ExtensionResultItem(icon='images/icon.png',
                                name="Project Search",
                                description="Search public projects in the entire GitLab platform",
                                highlightable=False,
                                on_enter=SetUserQueryAction("%s search " % keyword)),
            ExtensionResultItem(icon='images/icon.png',
                                name="My Projects",
                                description="List the projects you are a member of",
                                highlightable=False,
                                on_enter=SetUserQueryAction("%s projects " % keyword)),
            ExtensionResultItem(icon='images/icon.png',
                                name="My Projects (Starred)",
                                description="List your starred projects",
                                highlightable=False,
                                on_enter=SetUserQueryAction("%s starred " % keyword)),
            ExtensionResultItem(icon='images/icon.png',
                                name="My Groups",
                                description="List the groups you belong",
                                highlightable=False,
                                on_enter=SetUserQueryAction("%s groups " % keyword)),
            ExtensionResultItem(icon='images/icon.png',
                                name="GitLab Website",
                                description="Opens the GitLab website",
                                highlightable=False,
                                on_enter=OpenUrlAction(self.gitlab.url)),
            ExtensionResultItem(icon='images/icon.png',
                                name="GitLab Status",
                                description="Opens the GitLab status page",
                                highlightable=False,
                                on_enter=OpenUrlAction("https://status.gitlab.com")),
        ]

        return RenderResultListAction(menu)

    def show_my_menu(self, query):
        """ Show "My" Menu with links for Profile. Todos, PRs etc """

        gitlab_url = self.preferences["url"]

        # Authenticate the user, if its not already authenticated.
        if self.current_user is None:
            self.gitlab.auth()
            self.current_user = self.gitlab.user

        items = [
            ExtensionResultItem(icon='images/icon.png',
                                name='Logged in as %s' % self.current_user.username,
                                description='Open "Profile" page in Gitlab',
                                highlightable=False,
                                on_enter=OpenUrlAction('%s/profile' % gitlab_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Projects',
                                description='Open "Projects" page in Gitlab',
                                highlightable=False,
                                on_enter=OpenUrlAction('%s/dashboard/projects' % gitlab_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Groups',
                                description='Open "Groups" page on GitLab',
                                highlightable=False,
                                on_enter=OpenUrlAction('%s/dashboard/groups' % gitlab_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Snippets',
                                description='Open "Snippets" page on GitLab',
                                highlightable=False,
                                on_enter=OpenUrlAction('%s/dashboard/snippets' % gitlab_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Todos',
                                description='Open "Todos" page on GitLab',
                                highlightable=False,
                                on_enter=OpenUrlAction('%s/dashboard/todos' % gitlab_url)),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Issues',
                                description='Open "Issues" page on GitLab',
                                highlightable=False,
                                on_enter=OpenUrlAction(
                                    '%s/dashboard/issues?assignee_id=%s' % (gitlab_url, self.current_user.id))),
            ExtensionResultItem(icon='images/icon.png',
                                name='My Merge Requests',
                                description='Open "Merge Requests" page on GitLab',
                                highlightable=False,
                                on_enter=OpenUrlAction(
                                    '%s/dashboard/merge_requests?assignee_id=%s' % (gitlab_url, self.current_user.id))),
        ]

        if query:
            items = [p for p in items if query.lower()
                     in p.get_name().lower()]

        return RenderResultListAction(items)

    def search_projects(self, query, search_type):
        """ Search projects in GitLab """

        if search_type == PROJECTS_SEARCH_TYPE_MEMBER:
            projects = self.gitlab.projects.list(
                search=query, membership=1, order_by='name', sort='asc', simple=1, page=1, per_page=10)
        elif search_type == PROJECTS_SEARCH_TYPE_STARRED:
            projects = self.gitlab.projects.list(
                search=query, order_by='last_activity_at', sort='desc', starred=1, simple=1, page=1, per_page=10)
        else:
            projects = self.gitlab.projects.list(
                search=query, visibility='public', order_by='last_activity_at', sort='desc', simple=1, page=1, per_page=10)

        if not projects:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="No projects found matching your search criteria",
                    highlightable=False,
                    on_enter=HideWindowAction())

            ])

        items = []
        for project in projects:
            if project.description is not None:
                description = project.description.encode('utf-8')
            else:
                description = ''
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name=project.name.encode(
                    'utf-8'),
                description=description,
                highlightable=False,
                on_enter=OpenUrlAction(project.web_url))
            )

        return RenderResultListAction(items)

    def list_groups(self, query):
        """ Lists the groups the user belongs to """

        items = []
        groups = self.gitlab.groups.list(archived=0,
                                         search=query, order_by='name', sort='asc', page=1, per_page=10)

        if not groups:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="No groups found matching your search criteria",
                    highlightable=False,
                    on_enter=HideWindowAction())

            ])

        for group in groups:
            if group.description is not None:
                description = group.description.encode('utf-8')
            else:
                description = ''

            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name=group.name.encode(
                    'utf-8'),
                description=description,
                highlightable=False,
                on_enter=OpenUrlAction(group.web_url))
            )

        return RenderResultListAction(items)


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument()

        if query is None:
            return extension.show_menu()

        # Get the action based on the search terms
        search = re.findall(r"^search(.*)?$", query, re.IGNORECASE)
        repos = re.findall(r"^projects(.*)?$", query, re.IGNORECASE)
        groups = re.findall(r"^groups(.*)?$", query, re.IGNORECASE)
        starred = re.findall(r"^starred(.*)?$", query, re.IGNORECASE)
        my = re.findall(r"^my(.*)?$", query, re.IGNORECASE)

        try:
            if my:
                return extension.show_my_menu(my[0])

            if search:
                return extension.search_projects(search[0], PROJECTS_SEARCH_TYPE_PUBLIC)

            if repos:
                return extension.search_projects(repos[0], PROJECTS_SEARCH_TYPE_MEMBER)

            if starred:
                return extension.search_projects(starred[0], PROJECTS_SEARCH_TYPE_STARRED)

            if groups:
                return extension.list_groups(groups[0])

            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='Please select a valid option',
                                    highlightable=False,
                                    on_enter=HideWindowAction())
            ])

        except gitlab.GitlabError as e:
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='An error ocurred when connecting to GitLab',
                                    description=str(e),
                                    highlightable=False,
                                    on_enter=HideWindowAction())
            ])


class PreferencesEventListener(EventListener):
    """
    Listener for prefrences event.
    It is triggered on the extension start with the configured preferences
    """

    def on_event(self, event, extension):
        """ Initializes the GitLab client """
        extension.gitlab = gitlab.Gitlab(
            event.preferences['url'],
            private_token=event.preferences['access_token']
        )

        # save the logged in user.
        try:
            extension.gitlab.auth()
            extension.current_user = extension.gitlab.user
        except Exception as e:
            LOGGER.error(e)
            extension.current_user = None


class PreferencesUpdateEventListener(EventListener):
    """
    Listener for "Preferences Update" event.
    It is triggered when the user changes any setting in preferences window
    """

    def on_event(self, event, extension):
        if event.id == 'url':
            extension.gitlab.url = event.new_value
        elif event.id == 'access_token':
            extension.gitlab = gitlab.Gitlab(
                extension.preferences['url'],
                private_token=event.new_value
            )

            # save the logged in user.
            try:
                extension.gitlab.auth()
                extension.current_user = extension.gitlab.user
            except Exception as e:
                LOGGER.error(e)
                extension.current_user = None


if __name__ == '__main__':
    GitLabExtension().run()
