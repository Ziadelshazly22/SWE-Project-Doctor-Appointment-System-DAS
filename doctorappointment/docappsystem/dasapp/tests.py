from django.test import TestCase
from django.urls import reverse
from django.test import TestCase, Client
from django.urls import reverse
from dasapp.models import Appointment, DoctorReg, Page
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User
from dasapp.models import DoctorReg, Page

# Test Case for the Index View: This test case will check if the Index view is returning the correct template and context data.
class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.doctor = DoctorReg.objects.create(name='Test Doctor')
        self.page = Page.objects.create(
            address='Test Address',
            email='test@example.com',
            mobilenumber='+1234567890',
            aboutus='Test About Us'
        )

    def test_index_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('doctorview', response.context)
        self.assertIn('page', response.context)
        self.assertEqual(response.context['doctorview'].first(), self.doctor)
        self.assertEqual(response.context['page'].first(), self.page)

        # Test Case for the PROFILE View: This test case will check if the PROFILE view is returning the correct template and context data.
class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('profile')

    def test_profile_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'], self.user)

#Test Case for the CHANGE_PASSWORD View: This test case will check if the CHANGE_PASSWORD view is working correctly.
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import User

class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('profile')

    def test_profile_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn('user', response.context)
        self.assertEqual(response.context['user'], self.user)



# Test Case for the Login View: This test case will check if the Login view is working correctly.
class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')

    def test_login_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        response = self.client.post(self.url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

 # Test Case for the Logout View: This test case will check if the Logout view is working correctly.
class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('logout')

    def test_logout_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  # Redirect after logout
        self.assertFalse(response.wsgi_request.user.is_authenticated)

 #Test for create_appointment View: This test will check if the create_appointment view is working correctly
class CreateAppointmentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('create_appointment')
        self.doctor = DoctorReg.objects.create(name='Test Doctor')

    def test_create_appointment_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_appointment.html')

    def test_create_appointment_view_post(self):
        response = self.client.post(self.url, {
            'doctor': self.doctor.id,
            'date': '2024-12-05',
            'time': '10:00:00',
            'reason': 'Routine Checkup'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful appointment creation
        self.assertTrue(Appointment.objects.filter(doctor=self.doctor, reason='Routine Checkup').exists())

# Test Case for the UserSearchAppointments View: This test case will check if the UserSearchAppointments view is working correctly.
class UserSearchAppointmentsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.url = reverse('user_search_appointments')
        self.doctor = DoctorReg.objects.create(name='Test Doctor')
        self.appointment = Appointment.objects.create(
            user=self.user,
            doctor=self.doctor,
            date='2024-12-05',
            time='10:00:00',
            reason='Routine Checkup'
        )

    def test_user_search_appointments_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_search_appointments.html')
        self.assertIn('appointments', response.context)
        self.assertTrue(response.context['appointments'].filter(reason='Routine Checkup').exists())


# Test Case for the ViewAppointmentDetails View: This test case will check if the ViewAppointmentDetails view is working correctly.
class ViewAppointmentDetailsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')
        self.doctor = DoctorReg.objects.create(name='Test Doctor')
        self.appointment = Appointment.objects.create(
            user=self.user,
            doctor=self.doctor,
            date='2024-12-05',
            time='10:00:00',
            reason='Routine Checkup'
        )
        self.url = reverse('view_appointment_details', args=[self.appointment.id])

    def test_view_appointment_details_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_appointment_details.html')
        self.assertIn('appointment', response.context)
        self.assertEqual(response.context['appointment'], self.appointment)        