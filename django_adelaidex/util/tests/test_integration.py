from django.core.urlresolvers import reverse
from django_adelaidex.util.test import SeleniumTestCase, NoHTML5SeleniumTestCase

class UtilTestCase(SeleniumTestCase):
    def test_staticfiles(self):
        home_path = reverse('home')
    
        self.selenium.get('%s%s' % (self.live_server_url, home_path))

        # Ensure no severe browser errors (e.g. add_dynamic() not found)
        errors = self.get_browser_log('SEVERE')
        self.assertEqual(len(errors), 0)

        heading = self.selenium.find_elements_by_css_selector('h1')
        self.assertEqual(len(heading), 1)
        self.assertEqual(
            heading[0].text,
            'Hello World',
        )

        # js loaded by this page adds a dynamic message
        dynamic = self.selenium.find_elements_by_css_selector('div')
        self.assertEqual(len(dynamic), 1)
        self.assertEqual(
            dynamic[0].text,
            'javascript rocks'
        )
