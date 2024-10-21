import re

class Time:
    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = None
        Time.time_count += 1

    def __assign_format(self, pszFormat):
        """
        Checks pszFormat has correct value & assigns it to format
        Converts to upper case to avoid capitalization issues.
        """
        pszFormat = pszFormat.upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        else:
            return False

    def __is_24hour_format(self):
        return self.format == "24 HOURS"

    def _is_valid_time(self):
        if self.__is_24hour_format():
            return 0 <= self.hours <= 23 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59
        else:  # AM/PM format
            return 1 <= self.hours <= 12 and 0 <= self.minutes <= 59 and 0 <= self.seconds <= 59

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        """
        Assigns a time to the class after validation.
        """
        if not self.__assign_format(pszFormato):
            return False  # Invalid format

        self.hours = nHoras
        self.minutes = nMinutos
        self.seconds = nSegundos

        if not self._is_valid_time():
            return False  # Invalid time according to the format

        return True

    def get_time(self):
        """
        Returns the current time in string format.
        """
        if self.format == "24 HOURS":
            return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"
        else:
            return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        """
        Creates Time object from string (HH:MM:SS FORMAT).
        """
        pattern = r"(\d{2}):(\d{2}):(\d{2}) (AM|PM|24 HOURS)"
        match = re.match(pattern, time_string.upper())
        if not match:
            print("Invalid time string format.")
            return None
        
        hours, minutes, seconds, format_ = match.groups()
        time_obj = cls()
        if time_obj.set_time(int(hours), int(minutes), int(seconds), format_):
            return time_obj
        else:
            print("Invalid time values.")
            return None

    @staticmethod
    def is_valid_format(time_format):
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        return cls.time_count


def format_time_string(time_obj):
    """
    Function to return time as a string from a Time object.
    """
    if time_obj:
        return time_obj.get_time()
    else:
        return "No time set."


def main():
    current_time = None  # Initially no time set
    while True:
        print("\nMenu:")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena (formato HH:MM:SS)")
        print("4. Terminar")

        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            try:
                nHoras = int(input("Ingrese horas: "))
                nMinutos = int(input("Ingrese minutos: "))
                nSegundos = int(input("Ingrese segundos: "))
                pszFormato = input("Ingrese formato (AM, PM o 24 HOURS): ")

                if current_time is None:
                    current_time = Time()

                if current_time.set_time(nHoras, nMinutos, nSegundos, pszFormato):
                    print("Hora establecida correctamente.")
                else:
                    print("Error: Hora o formato no válidos.")
            except ValueError:
                print("Error: Entrada inválida, por favor ingrese números correctos.")
        
        elif choice == '2':
            if current_time:
                print(f"Hora actual: {format_time_string(current_time)}")
            else:
                print("No hay hora establecida.")

        elif choice == '3':
            time_string = input("Ingrese la hora en formato HH:MM:SS FORMAT: ")
            new_time = Time.from_string(time_string)
            if new_time:
                current_time = new_time
                print("Hora creada correctamente a partir de la cadena.")
            else:
                print("Error: La cadena de tiempo no es válida.")

        elif choice == '4':
            print("Terminando el programa.")
            break

        else:
            print("Opción inválida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
