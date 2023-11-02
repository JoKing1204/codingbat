from django.test import SimpleTestCase


class TestNearHundred(SimpleTestCase):
    def test_near_hundred(self):
        response = self.client.get("/Warmup-1/near-hundred/93/")
        self.assertContains(response, "True")

    def test_near_hundred_two(self):
        response = self.client.get("/Warmup-1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundred_three(self):
        response = self.client.get("/Warmup-1/near-hundred/89/")
        self.assertContains(response, "False")
        


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion(self):
        response = self.client.get("/Warmup-2/String-Splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_string_splosion_two(self):
        response = self.client.get("/Warmup-2/String-Splosion/abc/")
        self.assertContains(response, "aababc")
    
    def test_string_splosion_three(self):
        response = self.client.get("/Warmup-2/String-Splosion/ab/")
        self.assertContains(response, "aab")


class TestStringTwo(SimpleTestCase):
    def test_string_cat(self):
        response = self.client.get("/String-2/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_string_cat_two(self):
        response = self.client.get("/String-2/cat-dog/dogcat/")
        self.assertContains(response, "True")

    def test_string_cat_three(self):
        response = self.client.get("/String-2/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")

class TestLogicTwo(SimpleTestCase):
    def test_logic_two(self):
        response = self.client.get("/Logic-2/lone-sum/3/3/3/")
        self.assertContains(response, "0")

    def test_logic_three(self):
        response = self.client.get("/Logic-2/lone-sum/3/2/3/")
        self.assertContains(response, "2")
        
    def test_logic_four(self):
        response = self.client.get("/Logic-2/lone-sum/1/2/3/")
        self.assertContains(response, "6")