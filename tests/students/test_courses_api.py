import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student
from django.urls import reverse


@pytest.fixture
def base_url():

    return 'http://127.0.0.1:8000/api/v1/'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():

    def factory(*args, **kwargs):

        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():

    def factory(*args, **kwargs):

        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_course(client, course_factory):

    courses = course_factory(_quantity=2)
    url = reverse('courses-detail', args = [courses[0].id])
    response = client.get(url)
    
    assert response.status_code == 200
    assert response.data['id'] == courses[0].id

@pytest.mark.django_db
def test_list_course(client, course_factory):

    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == 200
    
    for i, c in enumerate(response.data):

        assert c['id'] == courses[i].id

@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    
    courses = course_factory(_quantity = 11)
    url = reverse("courses-list")+f'?name={courses[0].name}'
    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_filter_course_id(client, course_factory):

    courses = course_factory(_quantity = 11)
    url = reverse("courses-list")+f'?id={courses[0].id}'
    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['id'] == courses[0].id

@pytest.mark.django_db
def test_create_course(client):

    url = reverse('courses-list')
    response = client.post(url, {'name': 'test1',})
    assert response.status_code == 201

@pytest.mark.django_db
def test_update_course(client, course_factory):

    courses = course_factory(_quantity=15)
    url = reverse('courses-detail', args = [[courses[0].id]])
    response = client.patch(url, {'name': 'test55'})

    assert response.status_code == 200
    assert response.data['name'] == 'test55'


@pytest.mark.django_db
def test_update_course(client, course_factory):

    courses = course_factory(_quantity=15)
    url = reverse('courses-detail', args = [courses[0].id])
    response = client.delete(url)

    assert response.status_code == 204

















    



