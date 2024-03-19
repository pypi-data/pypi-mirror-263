#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# File          : basic
# Author        : Sun YiFan-Movoid
# Time          : 2024/2/16 20:12
# Description   : 
"""

import os
import pathlib
import re
import time
from typing import List

from movoid_function import reset_function_default_value
from RobotFrameworkBasic import robot_log_keyword, do_until_check, do_when_error, RfError
from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement

from ..common import BasicCommon


class SeleniumAction(BasicCommon):
    def __init__(self):
        super().__init__()
        self._check_element_attribute_change_value = None

    def selenium_take_full_screenshot(self, screenshot_name='python-screenshot.png'):
        return self.selenium_take_screenshot(image_name=screenshot_name)

    def selenium_click_element(self, click_locator, operate='click'):
        self.selenium_click_element_with_offset(click_locator, 0, 0, operate)
        return True

    @robot_log_keyword
    def selenium_click_element_with_offset(self, click_locator, x=0, y=0, operate='click'):
        tar_element = self.selenium_analyse_element(click_locator)
        self.action_chains.move_to_element_with_offset(tar_element, x, y)
        if operate == 'click':
            self.action_chains.click()
        elif operate in ('double_click', 'doubleclick'):
            self.action_chains.double_click()
        self.action_chains.perform()
        return True

    @robot_log_keyword
    def selenium_check_element_attribute(self, check_locator, check_attribute='innerText', check_value='', regex=True, check_bool=True):
        """
        检查所有元素中，是否存在一个属性满足要求的元素
        :param check_locator: 元素定位
        :param check_attribute: 属性名
        :param check_value: 属性值
        :param regex: 是否做正则匹配
        :param check_bool: 要求满足条件还是不满足条件的
        :return: 判定结果
        """
        tar_elements = self.selenium_find_elements_by_locator(check_locator)
        tar_exist = False
        for i_element, one_element in enumerate(tar_elements):
            tar_value = one_element.get_attribute(check_attribute)
            self.print(f'{check_attribute} of <{check_locator}>({i_element}) is:{tar_value}')
            if regex:
                check_result = bool(re.search(check_value, tar_value))
                self.print(f'{check_result}: <{check_value}> in <{tar_value}>')
            else:
                check_result = check_value == tar_value
                self.print(f'{check_result}: <{check_value}> == <{tar_value}>')
            tar_exist = tar_exist or check_result == check_bool
        self.print(f'check result is:{tar_exist}')
        return tar_exist

    @robot_log_keyword
    def selenium_find_elements_with_attribute(self, find_locator, find_value='', find_attribute='innerText', regex=True, check_bool=True) -> List[WebElement]:
        tar_elements = self.selenium_analyse_elements(find_locator)
        find_elements = []
        if find_attribute is None:
            find_elements = tar_elements
            self.print(f'find {len(find_elements)} elements only locator <{find_locator}>')
        else:
            self.print(f'find {len(tar_elements)} elements <{find_locator}> first')
            for i_element, one_element in enumerate(tar_elements):
                tar_value = one_element.get_attribute(find_attribute)
                self.print(f'{find_attribute} of <{find_locator}>({i_element}) is:{tar_value}')
                if regex:
                    check_result = bool(re.search(find_value, tar_value))
                    self.print(f'{check_result}: <{find_value}> in <{tar_value}>')
                else:
                    check_result = find_value == tar_value
                    self.print(f'{check_result}: <{find_value}> == <{tar_value}>')
                if check_result == check_bool:
                    find_elements.append(one_element)
            self.print(f'find {len(find_elements)} elements <{find_locator}> <{find_attribute}> is <{find_value}>(regex={regex},check={check_bool})')
        return find_elements

    @robot_log_keyword
    def selenium_find_element_with_attribute(self, find_locator, find_value='', find_attribute='innerText', regex=True, check_bool=True):
        find_elements = self.selenium_find_elements_with_attribute(find_locator, find_value=find_value, find_attribute=find_attribute, regex=regex, check_bool=check_bool)
        if len(find_elements) == 0:
            raise RfError(f'fail to find <{find_locator}> with <{find_attribute}> is <{find_value}>(re={regex},bool={check_bool})')
        return find_elements[0]

    @robot_log_keyword
    def selenium_get_locator_attribute(self, target_locator, target_attribute='innerText'):
        tar_element = self.selenium_find_element_by_locator(target_locator)
        return tar_element.get_attribute(target_attribute)

    @robot_log_keyword
    def selenium_new_screenshot_folder(self):
        screen_path = self.get_robot_variable("Screenshot_path")
        if screen_path:
            screen_pathlib = pathlib.Path(screen_path)
            if not screen_pathlib.exists():
                os.mkdir(screen_path)
                self.print('create dir : {}'.format(screen_path))

    @robot_log_keyword
    def selenium_delete_elements(self, delete_locator):
        elements = self.selenium_find_elements_by_locator(delete_locator)
        self.print(f'find {len(elements)} elements:{delete_locator}')
        for one_element in elements:
            self.selenium_execute_js_script('arguments[0].remove();', one_element)
        self.print(f'delete all {len(elements)} elements:{delete_locator}')

    @robot_log_keyword
    def selenium_input_delete_all_and_input(self, input_locator, input_text):
        self.selenium_lib.wait_until_page_contains_element(input_locator)
        input_element = self.selenium_analyse_element(input_locator)
        self.print(f'try to input ({str(input_text)}) by ({input_text})')
        input_text = str(input_text)
        self.print(f'find element:{input_element.get_attribute("outerHTML")},')
        now_str = input_element.get_attribute('value')
        self.print(f'element has text({len(now_str)}):{now_str}')
        for _ in now_str:
            input_element.send_keys(Keys.BACK_SPACE)
        for i in input_text:
            input_element.send_keys(i)
            time.sleep(0.01)
        self.print(f'input {input_text} success')
        self.selenium_wait_until_find_element_attribute(input_locator, input_text, 'value', regex=False)

    @robot_log_keyword
    def selenium_check_contain_element(self, check_locator, check_exist=True):
        find_elements = self.selenium_find_elements_by_locator(check_locator)
        find_elements_bool = len(find_elements) > 0
        self.print(f'we find {find_elements_bool}→{check_exist} {check_locator}')
        return find_elements_bool == check_exist

    @robot_log_keyword
    def selenium_check_contain_elements(self, check_locator, check_count=1):
        check_count = int(check_count)
        find_elements = self.selenium_find_elements_by_locator(check_locator)
        find_elements_num = len(find_elements)
        self.print(f'we find {find_elements_num}→{check_count} {check_locator}')
        return find_elements_num == check_count

    @robot_log_keyword
    def selenium_check_element_attribute_change_init(self, check_locator, check_attribute=''):
        tar_element = self.selenium_find_element_by_locator(check_locator)
        self._check_element_attribute_change_value = tar_element.get_attribute(check_attribute)
        self.print(f'we find {check_attribute} of {check_locator} is {self._check_element_attribute_change_value}')
        return False

    @robot_log_keyword
    def selenium_check_element_attribute_change_loop(self, check_locator, check_attribute=''):
        tar_element = self.selenium_find_element_by_locator(check_locator)
        temp_value = tar_element.get_attribute(check_attribute)
        re_bool = self._check_element_attribute_change_value == temp_value
        self.print(f'we find {check_attribute} of {check_locator} is {temp_value}{"==" if re_bool else "!="}{self._check_element_attribute_change_value}')
        return re_bool

    def always_true(self):
        return True

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(always_true, selenium_click_element_with_offset)
    def selenium_click_until_available(self):
        pass

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(selenium_click_element_with_offset, selenium_check_contain_element)
    def selenium_click_until_find_element(self):
        pass

    @reset_function_default_value(selenium_click_until_find_element)
    def selenium_click_until_not_find_element(self, check_exist=False):
        pass

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(selenium_click_element_with_offset, selenium_check_contain_elements)
    def selenium_click_until_find_elements(self):
        pass

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(selenium_click_element_with_offset, selenium_find_element_with_attribute)
    def selenium_click_until_find_element_attribute(self):
        pass

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(always_true, selenium_find_element_with_attribute)
    def selenium_wait_until_find_element_attribute(self):
        pass

    @robot_log_keyword
    @do_when_error(selenium_take_full_screenshot)
    @do_until_check(selenium_click_element_with_offset, selenium_check_element_attribute_change_loop, init_check_function=selenium_check_element_attribute_change_init)
    def selenium_click_until_attribute_change(self):
        pass
