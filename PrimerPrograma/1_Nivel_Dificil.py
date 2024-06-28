#ACTIVIDAD DE JUEGO BASADO EN IF Y ELSE CON UN O VARIAS PRGUNTAS DE ARITMETICAS Y UTILIZACION DE BOOL PARA OBJETOS


varita_Perdida = False
varita_Rota = False
capa_Invisible = False

numero_favorito = 12

print("\nVAMOS A JUGAR AL JUEGO DE HARRY POTTER Y VEREMOS COMO  TE VAS DE AQUI:"
      "\nSerá huir de la prisión de azkaban donde te encuentras ahora mismo estas solo pero debes huir como sea es la boda de tú hijo")


opcion = input("------------------------------------------------------------------"
               "\nQUÉ PREFIERES HACER:"
      "\n(1)SALIR POR LA ESCOTILLA SECRETA"
      "\n(2) DOBBY TE AYUDE A SALIR"
      "\n(3) HERMIONE VENGA A SALVARTE"
      "\n ACCION: ")

if opcion == "1":
      opcion2= input(""
                     "\n------------------------------------------------------------------"
                     "LA ESCOTILLA ESTABA ABIERTA Y ACABAS DE SALIR PERO HAY 2 DEMENTORES A PUNTO DE PILLARTE"
            "\n(1)INTENTAS DISTRAERLOS Y GANAR TIEMPO PARA UN NUEVO PLAN"
            "\n(2)INTENTAS ENFRENTARTE A ELLOS PERO ES MUY PELIGROSO NO TIENES TÚ VARITA"
            "\n(3)PASAR DE ELLOS Y BUSCAR OTRA SALIDA")

      if opcion2 == "1":
            print("\n------------------------------------------------------------------"
                  "\nLOS DEMENTORES VAN A POR UN MAGO REVOLTOSO Y PUEDES SALIR"
                  "\nAHORA ESTAS EN LA SALA CENTRAL Y DEBES DECIDIR QUE HACER")
            opcion_3 = input("(1)INTENTAR OCULTARTE Y BUSCAR ALGUNA MEJORA SALIDA"
                             "\n(2)TOMAR DE REHÉN A ALGUIEN E INTENATAR SALIR"
                             "\n(3)IR RÁPIDAMENTE A LA SALIDA CENTRAL"
                             "\n ACCION: ")

            if opcion_3 == "1":
                  print("\n------------------------------------------------------------------"
                        "\nVAS AHORA POR EL LADO IZQUIERDO PARACE DESPEJADO PERO VES A UN ELFO EN UNA RECEPCIÓN")
            elif opcion_3 == "2":
                  print("\nNO PARECE QUE NADIE VAYA EN BUSCA O SE ENTERÉ PARECE QUE ESTABA SOLO EL ELFO PERO TIENE UN SERIE DE OBJETOS INTERESANTES"
                        "\nHABÍA UNA CAPA  Y UNA VARITA CUAL PREFIERES")
                  opcion_04 = input("(1) LA VARITA "
                                    "\n(2) LA CAPA DE INVISIVILIDAD"
                                    "\n ACCION: ")
                  if opcion_04 == "1":
                        capa_Invisible = True
                        print("\nTENEMOS LA CAPA DE INVISIBLE PERFECTO NOS VAMOS DE AQUI Y BUSCAMOS LA SALIDA"
                              "\nTENEMOS PUESTA LA CAPA DE INVISIBLE .... AHORA ESTAMOS EN BUSCA DE UNA PUERTA O ALGO PARA SALIR")

                  elif opcion_04 == "2":
                        varita_rota = True
                        print("\nLA VARITA ESTÁ ROTA PERO NOS VAMOS DE AQUI EL ELFO SE PUEDE LEVANTAR EN CUALQUIER MOMENTO"
                              "\nESTAMOS AHORA OCULTO DETRAS DE UNA PUERTA PERO LA VARITA NO FUNCIONA INTENTAMOS REALIZAR UN HECHIZO PERO NOS AUTO EXPELLIARMUS Y NOS ATRAPAN"
                              "\n\n-------FIN--------"
                              "\nPIERDES")

            elif opcion_3 == "3":
                  print("\nESTAS INTENTADO SALIR PERO TE PILLAN Y TE MANDAN DE NUEVO A LA CELDA"
                        "\n\n-------FIN--------"
                        "\nPIERDES")

      elif opcion2 == "2":
            print("\nSON 2 ES UN LOCURA Y TE GANAN FÁCILMENTE Y PIERDES TODO HASTA TU LIBERTAD QUE TENIAS"
                  "\n\n-------FIN--------"
                  "\nPIERDES")
      elif opcion2 == "3":
            print("BUSCAS UNA SALIDA PERO NO PUEDES ESTA TODO MUY BIEN VIGILADO Y TE RINDES "
                  "\n\n-------FIN--------"
                  "\nPIERDES")

elif opcion == "2":
      print("DOBBY TE AYUDA A SALIR PERO NECESITAS RECUPERAR TÚ VARITA Y VAIS A INTENTAR RECUPERARLA EN LA SALA DE OBJETOS MALIGNOS")

      opcion02 = input("\nINTENTAS BUSCAR LA SALA PERO NO DAS CON ELLA Y DEBES HACER ALGO DIFERENTE PARA P0DER ENCONTRARLA"
                       "\n(1)MANDAS A DOBBY A QUE TE LO ENCUENTRE "
                       "\n(2)INTENTAS IR A BUSCAR INFORMACIÓN A LA OFICINA "
                       "\n(3)SIGUES BUSCANDO CON DOBBY HASTA ENCONTRAR LA SALA"
                       "\n ACCION: ")

      if opcion02 == "1":
            print("\nDOBBY INTENTA REALIZAR UNA INVOCACIÓN PERO LO PILLAN Y LO METEN PRESO Y TU ESTA SOLO Y FINALMENTE TE PILLAN A TI TAMBIÉN"
            "\n-------FIN--------"
            "\nPIERDES")
      elif opcion02 == "2":
            print("\n------------------------------------------------------------------"
                  "\nVAS A LA OFICINA PERO NO HAY NADIE SOLO UN ELFO CIEGO Y CON SUEÑO QUE JUSTO TIENE OBJETOS DE OTROS RECLUSOS")
            opcion_03 = input("\nVAMOS A INTENTAR QUE SE DUERMA Y BUSCAR ALGUN OBJETO QUE NO INTERSESE"
                              "\n(1)CANTAS UNA CANCIÓN PARA DORMRIR(NANA) EL ELFO SE DUERME Y VAS A POR LA BUSQUEDA DE OBJETOS"
                              "\n(2)INTENTAS IR PERO CON CAUTELA Y BUSCAR EN ENTRE LOS OBJETOS"
                              "\n ACCION: ")
            if opcion_03 == "1":
                  print("UNA VEZ DORMIDO BUSCAMS Y MIRA LO QUE TENEMOS UNA CAPA DE INVISIBILIDAD ")
                  opcion04 = input("(1)COGER LA CAPA"
                                   "\n(2)NO COGER  LA CAPA Y SALIR"
                                   "\n ACCION: ")

                  if opcion04 == "1":
                        capa_Invisible = True
                        print("\nTENEMOS LA CAPA DE VISIBILIDAD PERFECTO AHORA PODEMOS COLARNOS EN CUALQUIER SITIO Y OBTENER LA VARITA"
                              "\nAHORA ENTRE PASILLO Y PASILLOS OSCUROS VEMOS UNA PUERTA QUE PONE OBJETOS PERDIDOS PERO HAY 2 GUARDIAS DENTRO"
                              "\nNOS PONEMOS LA CAPA DE INVISILIBILIDAD Y ENTRAMOS CON UN HECHIZO DE DOBBY"
                              "\nENCONTRAMOS LA VARITA PERO ESTA EN UNA CAJA DE CRISTAL CON UN CONTRASEÑA")

                        opcion05 = input("(1) RESOLVER ACERTIJO"
                                         "\n(2)INTENTAR FORZAR LA CAJA"
                                         "\n ACCION: ")
                        if opcion05 == "1":
                              print("Es una pregunta de (12/6) * 5")
                              acertijo = (numero_favorito /6 )* 5
                              respuesta =  int(input("\n: "))

                              if respuesta == acertijo:
                                    print("\nPERFECTO ACABAS DE ABRIR LA CAJA Y PUEDES COGER TU VARITA"
                                          "\nAHORA PODEMOS SALIR Y VOLVER CON DOBBY"
                                          "\n AHORA ESTAMOS FUERA Y SALIMOS DE LA PRISION"
                                          "\n\n-------FIN--------"
                                          "\nGANAS FELICIDADES")
                              elif respuesta != acertijo:
                                    print("\nNO ES CORRECTO Y SONO LA ALARMA DEL FALLO, LOS GUARDIAS SE HAN DADO CUENTAS ESTAS EN PELIGRO"
                                          "\nENTRA DOBBY A SALVARTE PERO... AVADA KEDAVRA Y MORIS LOS 2"
                                          "\n\n-------FIN--------"
                                          "\nPIERDES")
                        elif opcion05 == "2":
                              print("\nHACES DEMASIADO RUIDO Y TE PILLA Y VUELVES ENCERRADO A LA CELDA, DOBBY HUYE Y TODO SE TERMINA"
                                    "\n\n-------FIN--------"
                                    "\nPIERDES")

            elif opcion_03 == "2":
                  print("\nFINALMENTE EL ELFO TE PILLA Y TERMINAS ARRESTADO "
                        "\n\n-------FIN--------"
                        "\nPIERDES")


      elif opcion02 == "3":
            print("\nDEREPENTE SALE UN DEMENTOR TRISTE Y OS AYUDA A SALIR Y TERMINAIS FUERA MUY FÁCIL HAS TENIDO SUERTE UN DEMENTOR TENÍA PENA Y NO SABÍA LO QUE HACÍA"
                  "\n\n-------FIN--------"
                  "\nGANAS FELICIDADES")


elif opcion == "3":
      capa_Invisible = True
      print("\n------------------------------------------------------------------"
            "\nHERMIONE VA POR LA NOCHE MÁS PROFUNDA, SON LAS 5 DE LA MAÑANA APARECE HERMIONE CON SU VARITA Y LA CAPA DE INVISILIBILIDAD Y REALIZA EL HECHIZO ALOHOMORA Y SALES"
            "\nHORA ESTAIS LOS 2 SOLOS PERO NECESITAS RECUPERAR TÚ VARITA, HERMIONE TE AYUDARÁ A ENCONTRARLA CON EL HECHIZO ACCIO PERO PARECE QUE NO VIENE TÚ VARITA"
            "\nLO RETIENE COMO ALGO MÁGICO DECIDIS INVESTIGAR Y VER QUE SUCEDE, OS TOPAIS CON UNA PUERTA QUE PONE OBJETOS PERSONALES"
            "\nENTRAIS Y LA VARITA ESTABA ATRAPADA POR UN CAJA INVISIBLE QUE TIENE UN HECHIZO ADIVINADOR , HERMIONE LO INTENTA PERO NO PUEDE NO SABE LA RESPUESTA ES TÚ TURNO"
            "\nDEBES DECIR CUAL ES EL NOMBRE DE HIJO DE DRACO MALFOY")
      opcion_02 = input("\n------------------------------------------------------------------"
                        "\n(1)CONSTANTIN MALFOY"
                        "\n(2)TERMIAN MALFOY"
                        "\n(3)SCORPIUS MALFOY"
                        "\n ACCION: ")
      if opcion_02 == "1":
            print("\nFALLASTE NO  ES LA RESPUESTA CORRECTA Y NÚMERO DE INTENTOS ALCANZÓ SU MÁXIMO NUMERO DE INTENTO Y EXPLOTA TODO Y TERMINAIS PRESOS LOS 2 "
                  "\n\n-------FIN--------"
                  "\nPIERDES")
      elif opcion_02 == "2":
            print("\nFALLASTE NO  ES LA RESPUESTA CORRECTA Y NÚMERO DE INTENTOS ALCANZÓ SU MÁXIMO NUMERO DE INTENTO Y EXPLOTA TODO Y TERMINAIS PRESOS LOS 2 "
                  "\n\n-------FIN--------"
                  "\nPIERDES")
      elif opcion_02 == "3":
            print("\nSE ABRE LA CERRADURA Y ACERTASTE AHORA TIENES TÚ VARITA Y LA CAPA DE INVISIBILIDAD LA PUERTA DE SALIDA ES MÁS FÁCIL DE SALIR"
                  "\n AHORA LOS 2 SALIS FÁCILMENTE"
                  "\n\n-------FIN--------"
                  "\nGANAS FELICIDADES")
