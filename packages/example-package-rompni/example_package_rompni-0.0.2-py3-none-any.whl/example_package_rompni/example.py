import json
import os
import traceback
import requests

def add_one(number):
    return number + 1

def add_two(number):
    return number + 2

def add_three(number):
    return number + 3

def add_four(number):
    return number + 4

def add_five(number):
    return number + 5

def test_env():
    return os.environ.get('ENV', 'development')

class statusClass: 
    HTTP_404_NOT_FOUND = 404
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_400_BAD_REQUEST = 400

def inyectar_doc_exedoc(
    ficha_id: str, 
    o_archivo, 
    log_params,
    settings,
):
    status = statusClass()
    """Realiza la llamada d GDMTT/EXEDOC"""
    log_params \
        .add_params("ficha_id", ficha_id) \
        .add_params("request_firma", o_archivo.request_firma) \
        .info("Se inicia la llamada a EXEDOC, en inyectar_doc_exedoc()")
    try:
        print("-----------")
        print("Entre al try de firma electronica avanzada")
        response_firma = requests.post(settings.URL_FIRMA_EXEDOC, json=o_archivo.request_firma)
        print(f"El url que se esta usando es {settings.URL_FIRMA_EXEDOC}")
        print("---------")
        log_params \
            .add_params('url', settings.URL_FIRMA_EXEDOC) \
            .info("Vuelve de EXEDOC, en inyectar_doc_exedoc()")
        print("Arme los params de log de firma electrónica avanzada y escribi un log")
        if response_firma.status_code == 200:
            #print("Estoy en el if de resultado = 200")
            response_request = json.loads(response_firma.text)
            log_params \
                .add_params("response_request", response_request) \
                .add_params("data", response_request) \
                .add_params("status", response_firma.status_code) \
                .add_params("URL_GDMTT", settings.URL_FIRMA_EXEDOC)
            log_params.info("Se guarda el archivo recibido y retornan respuesta")
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
                .warning('Envío con error a EXEDOC')

            if response_firma.status_code == 404:
                print("Estpy en error 404")
                mensaje = "No pudo firmar"
                log_params.info(f"{mensaje}, error {status.HTTP_404_NOT_FOUND}")
                return {
                    "data": mensaje,
                    "status": status.HTTP_404_NOT_FOUND
                }
            elif response_firma.status_code == 500:
                print("Estoy en error 500")
                mensaje = "Falló la firma"
                log_params.info(f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
                return {
                    "data": mensaje,
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            elif response_firma.status_code > 400:
                mensaje = "Falló la firma"
                log_params.info(f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
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
            .error(f'Fallo no controlado en la llamada de exedoc, se devuelve un error {status.HTTP_400_BAD_REQUEST}')
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "data": log,
        }
