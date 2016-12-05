# class UrlsTest(TestCase):
#     '''Test the index.html page'''
#
#     def test_indexPage(self):
#         """Tests the landing page"""
#         response = self.client.get("/frijay/")
#         self.assertEqual(response.status_code, 200)
#
#     '''Test the reservation.html page'''
#
#     def test_reservationPage(self):
#         """Tests the reservations page """
#         response = self.client.get("/frijay/reservations/")
#         self.assertEqual(response.status_code, 200)
#
#     '''Test the events.html page'''
#
#     def test_eventsPage(self):
#         """Tests the events page"""
#         response = self.client.get("/frijay/events/")
#         self.assertEqual(response.status_code, 200)
#
#     '''Test the about.html page'''
#
#     def test_aboutPage(self):
#         """Tests the about page"""
#         response = self.client.get("/frijay/about/")
#         self.assertEqual(response.status_code, 200)
#
#     '''Test the login.html page'''
#
#     def test_loginPage(self):
#         """Tests the login page"""
#         response = self.client.get("/frijay/login")
#         self.assertEqual(response.status_code, 200)
#
#     '''Test the signup.html'''
#
#     def test_signUpPage(self):
#         """Tests the signup page"""
#         response = self.client.get("/frijay/signup/")
#         self.assertEqual(response.status_code, 200)