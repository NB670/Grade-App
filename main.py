from studentvue import StudentVue
sv = StudentVue('470830', 'Lightning6452', 'https://md-mcps-psv.edupoint.com/PXP2_Login_Student.aspx?regenerateSessionId=True') 
gradebook=sv.get_gradebook()
print(gradebook)
