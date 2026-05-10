import requests
class CourseSelection:
    def __init__(self, cookie,  user_agent,authorization):
        self.base_url = 'https://bk.cup.edu.cn/course-selection-api/api/v1/student/course-select/add-predicate'
        self.headers = {
            'cookie': cookie,
            'user-agent': user_agent,
            'referer': 'https://bk.cup.edu.cn/course-selection/',
            'authorization': authorization
        }

    def add_course_request(self, student_assoc, course_select_turn_assoc, lesson):
        data = {
            'studentAssoc': student_assoc,
            'courseSelectTurnAssoc': course_select_turn_assoc,
            'coursePackAssoc': None,
            'requestMiddleDtos': [{'lessonAssoc': lesson, 'virtualCost': 0} ]
        }
        response = requests.post(url=self.base_url, headers=self.headers, json=data)
        return response

#修改参数处1
cookie = 'UM_distinctid=1909bca15eb1b0a-0bd20f01d2d31f-4c657b58-190140-1909bca15ec21e0; insert_cookie=40449351; cs-course-select-student-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXB3aXNkb20iLCJleHAiOjE3MzQ3MDM1MzQsInVzZXJuYW1lIjoiMjAyMzAxMDg4MSJ9.HbdGhlWfluEFVEp_5yn6Bglq3iq6RKaFSPnPXqHPZpQ'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXB3aXNkb20iLCJleHAiOjE3MzQ3MDM1MzQsInVzZXJuYW1lIjoiMjAyMzAxMDg4MSJ9.HbdGhlWfluEFVEp_5yn6Bglq3iq6RKaFSPnPXqHPZpQ'
course_selector = CourseSelection(cookie,  user_agent,authorization)

#修改参数处2
student_assoc = 
course_select_turn_assoc = 581
lessons = [ 96234,96281]  #课程的ID列表
for lesson in lessons:
# 发送请求
    responses = course_selector.add_course_request(student_assoc, course_select_turn_assoc, lesson)
    print(responses)
