asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]
asis_materi = {}
dias_alum = {}

for materia, alumno, fecha in asistencias:
    if materia not in asis_materi:
        asis_materi[materia] = set()
    asis_materi[materia].add(alumno)
    
    if alumno not in dias_alum:
        dias_alum[alumno] = set()
    dias_alum[alumno].add(fecha)
conteo_total = {}
for materia, alumno, fecha in asistencias:
    if alumno in conteo_total:
        conteo_total[alumno] += 1
    else:
        conteo_total[alumno] = 1

print(f"Alumnos por asignatura: {asis_materi}")
print(f"Días asistidos: {dias_alum}")