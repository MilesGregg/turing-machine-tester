from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from alive_progress import alive_bar

import time

MAX_RETEST = 50

def run_test(path):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    #set chromodriver.exe path
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.implicitly_wait(0.5)
    #launch URL

    tests_size = 8

    # startup all pages
    for i in range(1, tests_size):
        driver.execute_script(f"window.open('about:blank', {str(i)});")
        driver.switch_to.window(str(i))
        driver.get('https://turingmachinesimulator.com/')

    for i in range(6, 0, -1):
        driver.switch_to.window(str(i))

    # hashmap to keep track of the test cases
    # test_case: curr_index LINE NUM
    current = {
        1: 0,
        #2: 0,
        #3: 0,
        #4: 0,
        #5: 0,
        #6: 0,
        #7: 0
    }

    correct = {
        1: 1,
        #2: 0,
        #3: 0,
        #4: 0,
        #5: 0,
        #6: 0,
        #7: 0
    }

    done = {
        1: False,
        #2: False,
        #3: False,
        #4: False,
        #5: False,
        #6: False,
        #7: False
    }

    total_amount = 0

    for i in current.keys():
        total_amount += sum(1 for _ in open(path + 'problem' + str(i) + 'Tests.txt', 'r'))

    print(total_amount)

    with alive_bar(total_amount) as bar:
        while any(value == False for value in done.values()):
            for i in current.keys():
                bar()
                # switch to specific page
                driver.switch_to.window(str(i))

                # read file
                file = open(path + 'problem' + str(i) + 'Tests.txt', 'r')
                # check to make sure we aren't at the end
                if current[i] == sum(1 for _ in file):
                    done[i] = True
                    continue
                # rewind file
                file.seek(0)

                # load turing code into editor
                if current[i] == 0:
                    turing_code_file = open(path + 'problem' + str(i) + '.txt', 'r')
                    turing_lines = turing_code_file.readlines()

                    turing_code = '\n'.join(turing_lines)
                    turing_code_script = f'myCodeMirror.setValue({repr(turing_code)})'

                    driver.execute_script(turing_code_script)
                    driver.find_element(By.ID, 'loader').click()
                else: # CHECK ASSERTION HERE
                    #current_iteration += 1
                    #print('Curr Test: ', i)
                    #print(file.readlines()[current[i]-1].split(','))
                    prev_data_test = file.readlines()[current[i]-1].strip().split(',')
                    accepted = driver.execute_script('return document.getElementById("accepted_text").style.display') != 'none'
                    
                    for retest_n in range(MAX_RETEST):
                        accepted = driver.execute_script('return document.getElementById("accepted_text").style.display') != 'none'
                        try:
                            assert accepted == eval(prev_data_test[1]), f'Test Case failed let me retest (retest #{retest_n}) - Failed on: ' + str(prev_data_test[0]) + ' test case: ' + 'expected ' + str(prev_data_test[1]) + ' but got ' + str(accepted) + ", raw=" + driver.execute_script('return document.getElementById("accepted_text").style.display')
                            #current_iteration += 1
                            correct[i] += 1
                            break
                        except AssertionError as msg:
                            print(msg)
                            time.sleep(2)
                        if retest_n == MAX_RETEST - 1:
                            print(f"Max retests reached (MAX_RETEST = {MAX_RETEST}")
                            #exit(1)
                            break
                file.seek(0)

                # preform actions
                data = file.readlines()[current[i]].strip().split(',')

                driver.find_element(By.ID, 'input').clear()
                driver.find_element(By.ID, 'input').send_keys(data[0])
                try:
                    driver.find_element(By.ID, 'load_input').click()
                except:
                    time.sleep(1)
                    driver.find_element(By.ID, 'load_input').click()
                driver.execute_script('trans_speed = 0.0001')
                driver.find_element(By.ID, 'play').click()

                time.sleep(0.5)

                # increment count
                current[i] += 1

    for i in correct.keys():
        file = open(path + 'problem' + str(i) + 'Tests.txt', 'r')
        s = sum(1 for _ in file)
        print('Grade: ', str((correct[i] / s) * 100))
        print('sum: ', str(s))
        print('Correct: ', str(correct[i]))

if __name__ == '__main__':
    from glob import glob
    for g in glob("students/*/", recursive = True):
        run_test(g)
