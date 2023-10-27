from django.test import SimpleTestCase


class TestNearHundred(SimpleTestCase):
    def test_near_hundred(self):
        response = self.client.get("/Warmup-1/3/")
        self.assertContains(response, "False")

    def test_near_hundred_two(self):
        response = self.client.get("/Warmup-1/98/")
        self.assertContains(response, "True")

    def test_near_hundred_three(self):
        response = self.client.get("/Warmup-1/60/")
        self.assertContains(response, "False")
        


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion(self):
        response = self.client.get("/Warmup-2/Dog/")
        self.assertContains(response, "DDoDog")

    def test_string_splosion_two(self):
        response = self.client.get("/Warmup-2/racecar/")
        self.assertContains(response, "rraracraceracecracecaracecar")
    
    def test_string_splosion_three(self):
        response = self.client.get("/Warmup-2/Banana/")
        self.assertContains(response, "BBaBanBanaBananBanana")


class TestStringTwo(SimpleTestCase):
    def test_string_cat(self):
        response = self.client.get("/String-2/catcat/")
        self.assertContains(response, "False")

    def test_string_cat_two(self):
        response = self.client.get("/String-2/dogcat/")
        self.assertContains(response, "True")

    def test_string_cat_three(self):
        response = self.client.get("/String-2/catdog/")
        self.assertContains(response, "True")

class TestLogicTwo(SimpleTestCase):
    def test_logic_two(self):
        response = self.client.get("/Logic-2/3/3/3/")
        self.assertContains(response, "0")

    def test_logic_three(self):
        response = self.client.get("/Logic-2/4/5/1/")
        self.assertContains(response, "10")
        
    def test_logic_four(self):
        response = self.client.get("/Logic-2/1/2/3/")
        self.assertContains(response, "6")