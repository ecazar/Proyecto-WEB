INSERT INTO libros (id, isbn, titulo, autor, paginas, total_ejemplares, disponibles, portada_uri) VALUES
(1, '9780140449136', 'La Odisea', 'Homero', 400, 2, 1, 'https://www.loqueleo.com/co/uploads/2021/01/resized/360_la-odisea-1.JPG'),
(2, '9788420434170', 'Cien años de soledad', 'Gabriel García Márquez', 432, 1, 1, 'https://www.rae.es/sites/default/files/portada_cien_anos_de_soledad_0.jpg');

INSERT INTO recomendaciones (id, origen_id, recomendado_id, comentario) VALUES
(1, 1, 2, 'Si te gusta la mitología, te encantará el realismo mágico');

INSERT INTO ejemplares (id, libro_id) VALUES
(1, 1),
(2, 1),
(3, 2);

INSERT INTO usuarios (id, tipo, login, password, nombre, apellidos, correo, calle, numero, piso, ciudad, codigo_postal, estado) VALUES
(1, 'alumno', 'alumno01', '1234', 'Laura', 'Pérez', 'laura@example.com', 'Av. Siempre Viva', '123', '2', 'Quito', '170101', 'multado'),
(2, 'profesor', 'prof01', 'abcd', 'Carlos', 'Ramírez', 'carlos@example.com', 'Calle Falsa', '456', '3', 'Quito', '170202', 'activo');

INSERT INTO alumnos (id, telefono_padres) VALUES
(1, '0999999999');

INSERT INTO profesores (id, departamento) VALUES
(2, 'Lengua y Literatura');

INSERT INTO prestamos (id, usuario_id, ejemplar_id, fecha_prestamo, fecha_devolucion_esperada) VALUES
(1, 1, 1, CURRENT_DATE, CURRENT_DATE + INTERVAL '7 days');

INSERT INTO historico_prestamos (id, usuario_id, ejemplar_id, fecha_prestamo, fecha_devolucion) VALUES
(1, 2, 3, '2024-05-01', '2024-05-10');

INSERT INTO multas (id, usuario_id, fecha_inicio, dias_acumulados, fecha_fin) VALUES
(1, 1, CURRENT_DATE - INTERVAL '3 days', 3, NULL);

INSERT INTO historico_multas (id, usuario_id, fecha_inicio, fecha_fin, dias_acumulados) VALUES
(1, 2, '2024-04-01', '2024-04-05', 4);
