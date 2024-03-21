import logging


class AsanaControler():
    def __init__(self):
        self._client = None

    def set_config(self, config):
        import asana
        TOKEN = config.get("token", "")
        self._client = asana.Client.access_token(TOKEN)
        return self.is_connected()

    def get_name(self):
        return "Asana"

    def is_connected(self):
        if self._client:
            if user := self._client.users.get_user("me"):
                logging.info(f"Logged to {self.get_name()} as {user}")
            else:
                logging.error(f"Unable to connect to {self.get_name()} instance. Check your credentials.")
                return False

            if spaces := self._client.workspaces.get_workspaces():
                workspace_found = False
                project_found = False
                for s in spaces:
                    workspace_gid = s.get("gid", "")
                    if len(workspace_gid) > 0:
                        workspace_found = True
                        if projects := self._client.projects.get_projects_for_workspace(workspace_gid):
                            for p in projects:
                                project_found = True
                                break
                if workspace_found:
                    if project_found:
                        return True
                    else:
                        logging.error(f"Unable to list {self.get_name()} projects. Check your permissions.")
                else:
                    logging.error(f"Unable to list {self.get_name()} workspaces. Check your permissions.")
            else:
                logging.error(f"Unable to connect to {self.get_name()} instance. Check your credentials.")
        return False

    def get_data(self, include_coments=False):
        if not self._client:
            return None, None, None, None, None

        if workspaces := self._client.workspaces.get_workspaces():
            for w in workspaces:
                workspace_gid = w.get("gid", "")
                if projects := self._client.projects.get_projects_for_workspace(workspace_gid):
                    for p in projects:
                        project_gid = p.get("gid", "")
                        if tasks := self._client.tasks.get_tasks_for_project(project_gid, opt_fields=["name", "gid", "notes", "permalink_url"]):
                            for t in tasks:
                                comments = []
                                title = t.get("name", "")
                                task_gid = t.get("gid", "")
                                description = t.get("notes", "")
                                url = t.get("permalink_url", "")
                                if include_coments:
                                    if stories := self._client.stories.get_stories_for_task(task_gid):
                                        for s in stories:
                                            if s.get("type", "").lower() == "comment".lower():
                                                comment = s.get("text", "")
                                                comments.append(comment)
                                yield title, description, comments, url, task_gid

    def post_comment(self, task_gid, comment):
        if not self._client:
            return False
        if comment_status := self._client.stories.create_story_for_task(task_gid, {"type": "comment", "text": comment}):
            status = comment_status.get("text", "")
        return len(status) > 0
