import datetime
from ..domain.interfaces import ProcesadorPago

class BancoNacionalProcesador(ProcesadorPago):
    """
    Implementación concreta de la infraestructura.
    Simula un banco local escribiendo en un log.
    """
    def pagar(self, monto: float) -> bool:
        # SUSTITUYA "SU_NOMBRE" por su nombre y apellido real
        archivo_log = "pagos_locales_MIGUEL_ANGEL_CORREA_PIEDRAHITA.log"

        with open(archivo_log, "a") as f:
            f.write(f"[{datetime.datetime.now()}] Transaccion exitosa por: ${monto:.2f}\n")
        return True