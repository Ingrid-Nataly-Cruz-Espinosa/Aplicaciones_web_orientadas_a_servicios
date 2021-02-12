import web
import json
import random
futuro = {}
urls = (
    '/(.*)',
    'carta_zodiacal',
)
app = web.application(urls, globals())


class carta_zodiacal():
	def GET(self, zodiaco):
		try:
			dia = int(zodiaco[0:2])
			mes = int(zodiaco[3:5])
			print(dia, mes)


			if dia >= 24 and mes == 9 or mes == 10 and dia <= 23:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "LIBRA"
				futuro["FECHA"] = "24-DE-SEP-23 DE OCT"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Tu eres otra onda, quien pueda estar conntigo, se habrá ganado el premio mayor. Valorate que vales mucho, no tienes aguantar personas que no te valoran. Asi siempre FELIZ nunca INFELIZ", "Cuando aprendemos a vivir desde el alma, ocurren varias cosas. Tomamos conciencia de los exquisitos patrones y ritmos sincrónicos que gobiernan la vida» Deepak Chopra.", "La felicidad humana generalmente no se logra con grandes golpes de suerte, que pueden ocurrir pocas veces, sino con pequeñas cosas que ocurren todos los días» Benjamin Franklin.", "La felicidad humana generalmente no se logra con grandes golpes de suerte, que pueden ocurrir pocas veces, sino con pequeñas cosas que ocurren todos los días» Benjamin Franklin.", "La vida es una obra de teatro que no permite ensayos. Por eso, canta, ríe, baila, llora y vive intensamente cada momento de tu vida antes que el telón baje y la obra termine sin aplausos» Charles Chaplin", "«El amor es el significado último de todo lo que nos rodea. No es un simple sentimiento; es la verdad, es la alegría que está en el origen de toda creación» Rabindranath Tagor."])) 
				futuro["ELEMENTO"] = "AIRE"
				futuro["NUMERO DE LA SUERTE"] = "15, 8, 43, 3, 10, 40"
				futuro["COLOR"] = "ROSA. Es el color excelente de libra, por ser simbolo del cariño y la amistad."				 
				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "ARIES"
				futuro["FECHA"] = "MARZO 21 – ABRIL 20"
				futuro[
				    "TU HOROSCOPO"] = (random.choice([ "Que chidoo tu! Se vienen buenos proyectos para ti, por fin vas a tener suerte con una pareja y vas a seguir creciendo en tu ambito, ya suelta el pasado y se feliz, TODO TE AMAN. ", "Pies ¿para qué los quiero si tengo alas para volar» Frida Kahlo.", "Exponte a tu miedo más profundo; después de eso, el miedo no tiene poder, y el miedo a la libertad se encoge y desaparece. Eres libre» Jim Morrison.", "«El conocimiento tiene que ser mejorado, desafiado e incrementado constantemente, o se desvanece» Peter Drucker."]))
				futuro["ELEMENTO"] = " FUEGO"
				futuro["NUMERO DE LA SUERTE"] = "31, 11, 52, 5, 15, 25"
				futuro["COLOR"] = "El rojo no solo simboliza amor, sino también poder y ambición. Aries es el signo de fuego, así que también le queda los cálidos como anaranjado, dorados o amarillos"
				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "ACUARIO"
				futuro["FECHA"] = "ENERO 21 – FEBRERO 19"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Siempre te quejas de estar soltero, pero el que te tira la onda, siempre lo criticas y le encuntras defectos. Sigues enamorado de tu ex y por eso no encuentras algo bonito otra vez, eres muy atractivo y guap@.", "Todo hombre debe decidir si caminará a la luz del altruismo creativo o en la obscuridad del egoísmo destructivo Martin Luther King.", "«La falta de miedo es como un músculo. Sé por propia experiencia que cuanto más lo ejercitas más natural se convierte el no dejar que los miedos guíen tu vida» Arianna Huffington", "Un hombre solo tiene derecho a mirar a otro hacia abajo, cuando ha de ayudarle a levantarse» Gabriel García Márquez."]))
				futuro["ELEMENTO"] = " AIRE"
				futuro["NUMERO DE LA SUERTE"] = "45, 49, 32, 28, 2, 42"
				futuro["COLOR"] = "La calma y curiosidad de un Acuario se ve reflejada en el turquesa, pero también en tonos verdes de la naturaleza."

				result = json.dumps(futuro)
				return result

			elif dia >= 21 and mes == 4 or dia <= 21 and mes == 5:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "TAURO"
				futuro["Fecha"] = "ABRIL 21 – MAYO 21"
				futuro[
				    "TuHoroscopo"] = (random.choice(["Se extraña tu version sin sentimientos, asi nadien te hara daño y seras chido siempre. ya no te ilusiones tan rapido porque no t valoran y solo juegan contigo. Mejor solo que mal acompañado y ya deja de estar llorando a las 3am por alguien",  "Lo que no te mata, te hace más fuerte» Friedrich Nietzche.", "Nuestra recompensa se encuentra en el esfuerzo y no en el resultado. Un esfuerzo total es una victoria completa» Mahatma Gandhi.","Ganas fuerza, coraje y confianza en cada experiencia en la que realmente te detienes a mirar al miedo en la cara. Eres capaz de decirte a ti mismo ‘he vivido este horror. Puedo tomar la siguiente cosa que viene’» Eleanor Roosevelt."])) 
				futuro["Elemento"] = " Tierra"
				futuro["Numero"] = "23, 13, 52, 52, 5, 15, 27"
				futuro["Color"] = "Son independientes y no dejan que nada se interponga en su camino hacia las metas, así que los tonos morados son para ellos. "

				result = json.dumps(futuro)
				return result

			elif dia >= 22 and mes == 5 or dia <= 22 and mes == 6:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "GEMINIS"
				futuro["Fecha"] = "MAYO 22 – JUNIO 22"
				futuro[
				    "TuHoroscopo"] = (random.choice(["Por fuera te vez bien inocente, linda y eduacada. Si vieras que eres medio cambiante de genero y que te gusta la cervezas banquetera y tu no te andas con rodeos, todo mundo se enamoria de ti. Esta semana bajaras de peso, tendras dinero y conoceras un nuevo juguete, bueno un nuevo ligue.", "«Me gustan los amigos que tienen pensamientos independientes, porque suelen hacerte ver los problemas desde todos los ángulos» Nelson Mandela.","La vida es como los otros juegos, se convierte en diversión cuando uno se da cuenta de que es sólo un juego» Nerijus Stasiulis.", "La imaginación es más importante que el conocimiento. El conocimiento es limitado y la imaginación circunda el mundo» Albert Einstein.", "Las palabras son pedazos de afecto que transportan a veces un poco de información» Boris Cyrulnik."]))
				futuro["Elemento"] = " Aire"
				futuro["Numero"] = "12, 7, 53, 18, 21, 54"
				futuro["Color"] = "El amarillo, con toda su luz y energía, ayuda al geminiano a ser organizado con sus cosas y a pensar de manera clara y racional. "
            
				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 6 or dia <= 23 and mes == 7:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "CANCER"
				futuro["FECHA"] = "JUNIO 23 – JULIO 23"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["NO SE TE OCURRA TIRARLE LA ONDA A UN CANCER. Son fieles a alguien que ni los quiere y andan sufriendo por puras cosas ue no. Son muy buena onda pero estan locos. pero siempre tendran mucho dinero y exito en su vida", "«Ser humano supone una experiencia corporal y anímica, única para cada persona […] no hay nadie igual a otro. Cada uno de nosotros posee su propia historia, que es única, y la realización de esta historia entrará en relación directa con el hecho de sí hemos elegido el sendero con el corazón» Jean Shinoda Bolen.", "«La familia es un complemento nuestro, complemento mayor que nosotros, anterior a nosotros y que nos sobrevivirá con lo mejor de nosotros» Alphonse de Lamartine.", "«El amor es intensidad y por esto es una distensión del tiempo: estira los minutos y los alarga como siglos» Octavio Paz."]))
				futuro["ELEMENTO"] = " Agua"
				futuro["NUMERO DE LA SUERTE"] = "1, 2, 16, 40, 22, 49"
				futuro["COLOR"] = "El blanco hará sentir a Cáncer protegido y libre de tensiones en su vida. También a Cáncer les queda bien colores del mar, como azul clarito, gris claro o tonos verde claros"
 
				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 7 or dia <= 22 and mes == 8:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "LEO"
				futuro["FECHA"] = "JULIO 23–AGOSTO 22"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Tus vacaciones siemre estan bien aburridas, ya mejor regra con tu ex, pero nadamas para confundirlo y reirte mil de el jajajajaja. Eres la lo mero chido que ogullo ser tu", "«Con el tiempo y la madurez, descubrirás que tienes dos manos; una para ayudarte a ti misma y otra para ayudar a los demás» Audrey Hepburn", "Si tus acciones inspiran a otros a soñar más, aprender más, hacer más y convertirse en algo más, entonces eres un líder» John Quincy Adams.", "Después de escalar una montaña muy alta, descubrimos que hay muchas otras montañas por escalar» Nelson Mandela."]))
				futuro["TU ELEMENTO"] = "Fuego"
				futuro["NUMERO DE LA SUERTE"] = "37, 19, 5, 16, 9, 50"
				futuro["COLOR"] = "Un Leo que busque tener éxito en el trabajo, debe usar naranja. Este tono ayuda a sentir a la gente más alegre y aleja la depresión. " 

				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "VIRGO"
				futuro["FECHA"] = "AGOSTO 23 – SEPTIEMBRE 22"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["ya aprende a soltar acepta que esa persona, que ya tiene otra persona y que eres mucha cosa para esa persona, Mejores cosas vendran, los virgos siempre salen adelante contra todo",  "Cuando sepas una cosa sostén que la sabes; cuando no la sepas, confiesa que no la sabes. En eso está la característica del conocimiento» Confucio", "«La inteligencia conoce todas las cosas y ordenó todas las cosas que van a ser y las que fueron y las que son ahora y las que no son» Anaxágoras", "Hoy te sentirás mucho mejor y recibirás gratificaciones o regalos, también la ayuda de alguien. Se materializarán algunos proyectos, además, te encontrarás en buena forma intelectual; sin embargo, es necesario que dejes que tus sentimientos ocupen su lugar y que tu corazón hable... A veces, te olvidas de esta faceta de la vida.", "Si he hecho descubrimientos invaluables, ha sido más por tener paciencia que cualquier otro talento» Isaac Newton"]))
				futuro["ELEMTO"] = "TIERRA"
				futuro["NUMERO DE LA SUERTE"] = "6, 31, 14, 15, 53, 46"
				futuro["COLOR"] = "Verde, tono de inteligencia y madurez, como los Virgo. Y el marrón es un color que se relaciona mucho con la fertilidad, de ahí su conexión con Virgo, el único representado por una mujer en el Zodiaco. "
				result = json.dumps(futuro)
				return result

			elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "ESCORPIO"
				futuro["FECHA"] = "OCTUBRE 23 – NOVIEMBRE 21"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Todos te odian por guapo, deja que su odio los consuma deja que hablen. A ti esta semana te ira muy bien te pagaran mucho dinero, y tendras un cuerpazo, tu ex te va a rogar. Llego tu momento de brillar.",  "Un buen líder lleva a las personas a donde quieren ir. Un gran líder las lleva a donde no necesariamente quieren ir, pero deben de estar» Rosalynn Carter.", "Creo en la determinación humana. A lo largo de la historia se ha comprobado que la voluntad humana es más poderosa que las armas» Dalai Lama.", "Cuando se discute no existe superior, ni inferior, ni títulos, ni edad, ni nombre: sólo cuenta la verdad; delante de ella todo el mundo es igual» Romain Rolland."])) 
				futuro["ELEMENTO"] = "Agua"
				futuro["NUMERO DE LA SUERTE"] = "31, 43, 22, 13, 40, 42"
				futuro["COLOR"] = "Por ser un signo muy fuerte, con carácter y determinación, les quedan colores asociados al misterio, como rojos oscuros, tonos vino y marrones. "
				result = json.dumps(futuro)
				return result

			elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
				futuro = {}
				futuro["SIGNO ZODIACAL"] = "SAGITARIO"
				futuro["FECHA"] = "NOVIEMBRE 22 - DICIEMBRE 21"
				futuro[
				    "TU HOROSCOPO"] = (random.choice(["Volviste a presumir a la persona equivocada, te fijas en puras personas que no te valoran, inestables que no saben que quieren. Date un tiepo de estar solo y conocerte porque sino vas a tener mala suerte en el amor siempre. Podrias ser mas bueno.", "No dejes apagar el entusiasmo, virtud tan valiosa como necesaria; trabaja, aspira, tiende siempre hacia la altura» Ruben Darío.", "El propósito de la vida es vivirla, saborear la experiencia al máximo, llegar con entusiasmo y sin temor a una experiencia más nueva y rica» Eleanor Roosevelt."])) 
				futuro["ELEMENTO"] = "FUEGO"
				futuro["NUMERO DE LA SUERTE"] = "20, 37, 41, 34"
				futuro["COLOR"] = "El azul ayuda a la tranquilidad de un Sagitario que, por ser un signo de fuego, quiere estar en constante movimiento."
				result = json.dumps(futuro)
				return result
		except:
			futuro = {}
			futuro["TU FUTURO"] = "EL FUTURO: " + str(zodiaco)
			futuro["ERROR DE FUTURO"] = "ERROR DE VALOR, ESTAS INVOCANDO AL DEMONIO"
			futuro[
			    "LISTO LEEMOS TU FUTURO"] = "FECHA DE NACIMIENTO:  DD/MM/AAAA"
			result = json.dumps(futuro)
			return result


if __name__ == "__main__":
	app.run()