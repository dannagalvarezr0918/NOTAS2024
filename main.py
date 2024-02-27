import modulos.gestoralumnos as st
import os
if __name__ == '__main__':
    alumnos = {}
    st.AddsStudent(alumnos)
    # st.AddsStudent(alumnos)
    # st.ListData(alumnos)
    # st.DelEstudent(alumnos)
    # st.DelByName(alumnos)
    os.system('cls')
    st.AddGrades(alumnos)