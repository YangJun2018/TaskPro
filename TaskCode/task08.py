__author__ = 'Administrator'


def teacher_info(path):
    teacher={}
    with open(path,mode="r",encoding="utf8") as t:
        mid=t.readlines()
        for i in range(0,len(mid)):
            if i>0:
                id=int(mid[i].split(";")[0].strip())
                real_name=mid[i].split(";")[4].strip()
                cache={id:real_name}
                teacher.update(cache)
            else:
                id=mid[i].split(";")[0].strip()
                real_name=mid[i].split(";")[4].strip()
                cache={id:real_name}
                teacher.update(cache)

    t.close()
    return teacher


def course_info(path):
    course={}
    with open(path,mode="r",encoding="utf8") as c:
        mid=c.readlines()
        for i in range(0,len(mid)):
            if i>0:
                id=int(mid[i].split(";")[0].strip())
                course_name=mid[i].split(";")[1].strip()
                cache={id:course_name}
                course.update(cache)
            else:
                id=mid[i].split(";")[0].strip()
                course_name=mid[i].split(";")[1].strip()
                cache={id:course_name}
                course.update(cache)

    c.close()
    return course


def teacher_course(path0,path1,path2,path3):
    course=course_info(path2)
    teacher=teacher_info(path3)
    with open(path0) as t:
        mid=t.readlines()
        for i in range(0,len(mid)):
            if i>0:
               teacher_id=int(mid[i].split(";")[0])
               course__id=int(mid[i].split(";")[1])
               with open(path1,'a',encoding='utf8') as f:
                   teacher_name=str(teacher[teacher_id]+":").ljust(10)
                   course_name=str(course[course__id]).center(20)
                   data=teacher_name+course_name
                   f.write(data+"\n")
                   f.close()
            else:
                with open(path1,'w',encoding='utf8') as f:
                    title_name="老师姓名:".ljust(10)
                    title_course="课程名".center(20)
                    title=title_name+title_course
                    f.write(title+"\n")
                    f.close()

    t.close()
    return True


path=["G:\\PythonTask\\AutoTest\\localtask\\TaskFile\\teacher.txt",
      "G:\\PythonTask\\AutoTest\\localtask\\TaskFile\\course.txt",
      "G:\\PythonTask\\AutoTest\\localtask\\TaskFile\\t_c_info.txt",
      "G:\\PythonTask\\AutoTest\\localtask\\TaskFile\\teacher_course.txt"]

teacher_course(path[3],path[2],path[1],path[0])
