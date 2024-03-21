import json
import traceback
import requests

def setLogSistema(log_params, log, type_log,  set_log_sistema):
    """
    Esta función se encarga de setear el log en el sistema y en la base de datos
    """
    set_log_sistema(
        log_params.view,
        log_params.method,
        log_params.function, 
        log,	
        log_params.params,
        type_log,
        log_params.trace,
        log_params.stack
    )

class statusClass: 
    HTTP_404_NOT_FOUND = 404
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_400_BAD_REQUEST = 400

def inyectar_doc_exedoc(
    ficha_id: str, # id de la ficha
    o_archivo,  # objeto de Archivo
    log_params, # objeto de SeimLogSistema
    settings, # objeto de settings
    set_log_sistema # función de set_log_sistema
):
    """
    Realiza la llamada de GDMTT/EXEDOC.

    
    Argumentos
    ----------
    - ``ficha_id`` (str) : str  id de la ficha
    - ``o_archivo`` (Archivo) :  objeto de Archivo
    - ``log_params`` (SeimLogSistema) : objeto de SeimLogSistema
    - ``settings`` : objeto de settings
    - ``set_log_sistema`` (function) función de set_log_sistema para escribir en el log del sistema

    
    Info
    ----
    - el argumento ``set_log_sistema`` se debe importar de la siguiente manera (ejemplo):
        from polls.services.set_log_sistema import set_log_sistema


           
    Retorno
    -------
    - ``data`` (dict) : diccionario con la respuesta de la llamada a EXEDOC
    - ``status`` (int) : el estado de la respuesta
    - ``URL_GDMTT`` (str|None) : la url de la llamada a EXEDOC
    """
    status = statusClass()
    log_params \
        .add_params("ficha_id", ficha_id) \
        .add_params("request_firma", o_archivo.request_firma)
        #.info("Se inicia la llamada a EXEDOC, en inyectar_doc_exedoc()")

    setLogSistema(log_params, "Se inicia la llamada a EXEDOC, en inyectar_doc_exedoc()", 'INFO', set_log_sistema)
    
    try:
        print("-----------")
        print("Entre al try de firma electronica avanzada")
        response_firma = requests.post(settings.URL_FIRMA_EXEDOC, json=o_archivo.request_firma)
        print(f"El url que se esta usando es {settings.URL_FIRMA_EXEDOC}")
        print("---------")
        log_params \
            .add_params('url', settings.URL_FIRMA_EXEDOC) \
            #.info("Vuelve de EXEDOC, en inyectar_doc_exedoc()")
        setLogSistema(log_params, "Vuelve de EXEDOC, en inyectar_doc_exedoc()", 'INFO', set_log_sistema)

        print("Arme los params de log de firma electrónica avanzada y escribi un log")
        if response_firma.status_code == 200:
            #print("Estoy en el if de resultado = 200")
            response_request = json.loads(response_firma.text)
            log_params \
                .add_params("response_request", response_request) \
                .add_params("data", response_request) \
                .add_params("status", response_firma.status_code) \
                .add_params("URL_GDMTT", settings.URL_FIRMA_EXEDOC)
            #log_params.info("Se guarda el archivo recibido y retornan respuesta")

            setLogSistema(log_params, "Se guarda el archivo recibido y retornan respuesta", 'INFO', set_log_sistema)
            return {
                "data": response_request,
                "status": response_firma.status_code,
                "URL_GDMTT": settings.URL_FIRMA_EXEDOC
            }
        else:
            print("Ocurrió un envío con error a exedoc")
            log_params \
                .add_params("response_firma", response_firma) \
                .add_params("response_firma.status_code", response_firma.status_code) \
                #.warning('Envío con error a EXEDOC')

            setLogSistema(log_params, "Envío con error a EXEDOC", 'WARNING', set_log_sistema)

            if response_firma.status_code == 404:
                print("Estpy en error 404")
                mensaje = "No pudo firmar"
                #log_params.info(f"{mensaje}, error {status.HTTP_404_NOT_FOUND}")
                setLogSistema(log_params, f"{mensaje}, error {status.HTTP_404_NOT_FOUND}", 'INFO', set_log_sistema)
                return {
                    "data": mensaje,
                    "status": status.HTTP_404_NOT_FOUND
                }
            elif response_firma.status_code == 500:
                print("Estoy en error 500")
                mensaje = "Falló la firma"
                #log_params.info(f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
                setLogSistema(log_params, f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}", 'INFO', set_log_sistema)
                return {
                    "data": mensaje,
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            elif response_firma.status_code > 400:
                mensaje = "Falló la firma"
                #log_params.info(f"{mensaje},error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
                setLogSistema(log_params, f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}", 'INFO', set_log_sistema)
                return { 
                    "data": mensaje,
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
    except Exception as exception:
        log = f'Se produjo intentar firmar documento de ficha: {ficha_id}'
        log_params \
            .add_params('exception', exception.__str__()) \
            .add_params('mensaje', log) \
            .set_traceback('\n '.join(traceback.format_exc().splitlines()), ''.join(traceback.format_stack())) \
            #.error(f'Fallo no controlado en la llamada de exedoc, se devuelve un error {status.HTTP_400_BAD_REQUEST}')
        
        setLogSistema(log_params, f'Fallo no controlado en la llamada de exedoc, se devuelve un error {status.HTTP_400_BAD_REQUEST}', 'ERROR', set_log_sistema)
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "data": log,
        }
