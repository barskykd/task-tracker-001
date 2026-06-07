from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model


class TestUnauthenticated(TestCase):
    def test_unauthenticated_redirects_to_login(self):
        response = self.client.get("/")
        assert response.status_code == 302


class TestTasksApi(TestCase):
    fixtures = ["sample_data.json"]

    def setUp(self):
        self.admin_user = get_user_model().objects.get(username='alice')
        self.client.force_login(self.admin_user)

    def test_index_page(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_list_task(self):
        response = self.client.get("/tasks/")
        assert len(response.json()) == 7

    def test_read_task(self):
        response = self.client.get("/tasks/5/")
        assert response.status_code == 200
        task = response.json()
        assert task["id"] == 5
        assert task["title"] == "Fix login page CSS"
        assert task["created_by"]["id"] == 2
        assert task["assigned_to"]["id"] == 3
        assert task["status"] == 0
        assert task["status_display"] == "In Progress"

    def test_delete_task(self):
        response = self.client.delete("/tasks/5/")
        assert response.status_code == 204

    def test_update_task(self):
        response = self.client.patch(
            "/tasks/5/", {"status": 1}, content_type='application/json')
        assert response.status_code == 200, response.content

        response = self.client.get("/tasks/5/")
        assert response.status_code == 200
        task = response.json()
        assert task["id"] == 5
        assert task["title"] == "Fix login page CSS"
        assert task["created_by"]["id"] == 2
        assert task["assigned_to"]["id"] == 3
        assert task["status"] == 1
        assert task["status_display"] == "Finished"

    def test_add_task(self):
        response = self.client.post(
            "/tasks/", {"title": "TestTask"}, content_type='application/json')
        assert response.status_code == 201, response.content
        task = response.json()
        assert task["title"] == "TestTask"
        assert task["created_by"]["id"] == self.admin_user.pk
        assert task["assigned_to"] is None
        assert task["status"] == 0
        assert task["status_display"] == "In Progress", task


class TestCommentaryApi(TestCase):
    fixtures = ["sample_data.json"]

    def setUp(self):
        self.admin_user = get_user_model().objects.get(username='bob')
        self.client.force_login(self.admin_user)

    def test_list_comments(self):
        response = self.client.get("/commentaries/", {"task_id": 1})
        assert response.status_code == 200, response.content
        comments = response.json()
        assert len(comments) == 3
        first_comment = comments[0]
        assert first_comment["author"]["id"] == 3, first_comment
        assert first_comment["author"]["username"] == "bob", first_comment
        assert first_comment['text'] == 'I can help with the Docker part.'

    def test_post_comment(self):
        response = self.client.post(
            "/commentaries/", {"task": 1, "text": "test_text"})
        assert response.status_code == 201, response.content
        comment = response.json()
        assert comment["author"]["id"] == self.admin_user.pk

        response = self.client.get("/commentaries/", {"task_id": 1})
        assert response.status_code == 200, response.content
        comments = response.json()
        assert len(comments) == 4

    def test_delete_comment_no_allowed(self):
        response = self.client.delete("/commentaries/1/")
        assert response.status_code == 405

    def test_update_comment_no_allowed(self):
        response = self.client.patch("/commentaries/1/")
        assert response.status_code == 405
