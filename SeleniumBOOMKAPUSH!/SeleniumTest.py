# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class PythonOrgSearch(unittest.TestCase):

    

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://127.0.0.1:8000"

#    def test_search_in_python_org(self):
 #       driver = self.driver
  #      driver.get("http://www.python.org")
   #     self.assertIn("Python", driver.title)
    #    elem = driver.find_element_by_name("q")
     #   elem.send_keys("pycon")
      #  elem.send_keys(Keys.RETURN)
       # assert "No results found." not in driver.page_source
        
        # malicia
            
    def test_editar_propietario(self):
        driver = self.driver
        driver.get(self.base_url + "/index/")
        driver.find_element_by_link_text("Propietarios").click()
        driver.find_element_by_xpath("//tr[2]/td[6]/a/i").click()
        driver.find_element_by_id("id_nomb_prop").clear()
        driver.find_element_by_id("id_nomb_prop").send_keys("Crisis de Identidad")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_link_text("Propietarios").click()
        
    #def test_editar_estacionamiento(self):
     #   pass
    
    #def test_parametrizar_estacionamiento(self):
     #   pass
    
    #def test_reparametrizar_estacionamiento(self):
     #   pass
    
    def consultar_reserva(self):
        driver = self.driver
        driver.get(self.base_url + "/index/")
        driver.find_element_by_link_text("Reservas").click()
        driver.find_element_by_link_text("Consultar Reservas").click()
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("44444444")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        Select(driver.find_element_by_id("id_cedulaTipo")).select_by_visible_text("E")
        driver.find_element_by_id("id_cedula").clear()
        driver.find_element_by_id("id_cedula").send_keys("33333333")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        Select(driver.find_element_by_id("id_cedulaTipo")).select_by_visible_text("V")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
 
    def test_consultar_billetera(self):
        driver = self.driver
        driver.get(self.base_url + "/index/")
        driver.find_element_by_link_text(u"Billetera Electrónica").click()
        driver.find_element_by_link_text("Consultar Billetera Electronica").click()
        driver.find_element_by_id("id_id").clear()
        driver.find_element_by_id("id_id").send_keys("4")
        driver.find_element_by_id("id_pin").clear()
        driver.find_element_by_id("id_pin").send_keys("1111")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        
    def test_cambiar_pin(self):
        driver = self.driver
        driver.get(self.base_url + "/index/")
        driver.find_element_by_link_text(u"Billetera Electrónica").click()
        driver.find_element_by_link_text(u"Cambiar Contraseña").click()
        driver.find_element_by_id("id_id").clear()
        driver.find_element_by_id("id_id").send_keys("4")
        driver.find_element_by_id("id_pin").clear()
        driver.find_element_by_id("id_pin").send_keys("1111")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_css_selector("a > button.btn.btn-primary").click()
        driver.find_element_by_id("id_pin").clear()
        driver.find_element_by_id("id_pin").send_keys("1111")
        driver.find_element_by_id("id_pin_verificar").clear()
        driver.find_element_by_id("id_pin_verificar").send_keys("1111")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

    
    def test_consultar_historial(self):
        driver = self.driver
        driver.get(self.base_url + "/index/")
        driver.find_element_by_link_text(u"Billetera Electrónica").click()
        driver.find_element_by_link_text("Consultar Historial").click()
        driver.find_element_by_id("id_id").clear()
        driver.find_element_by_id("id_id").send_keys("4")
        driver.find_element_by_id("id_pin").clear()
        driver.find_element_by_id("id_pin").send_keys("1111")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()

    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()