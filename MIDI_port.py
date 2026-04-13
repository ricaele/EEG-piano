import mido
from datetime import datetime
import time
import csv

input_ports = mido.get_input_names()
print(input_ports)

if not input_ports:
    print("Nenhuma porta MIDI conectada!")
else:
    start_timestamp = datetime.now().strftime("%Y-%m-%d %H.%M.%S.%f")[:-3]
    with mido.open_input(input_ports[0]) as port, open(f"midi_capture_{start_timestamp}.csv", "w", newline="") as f:
        
        writer = csv.writer(f)
        writer.writerow(["timestamp", "type", "note", "velocity"])  # cabeçalho
        
        print(f"Porta conectada: {input_ports[0]}")
        print("Pronto para capturar notas... pressione Ctrl+C para sair.")
        
        try:
            while True:
                for msg in port.iter_pending():
                    if msg.type in ['note_on', 'note_off']:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                        
                        print(f"{timestamp} | {msg.type} | Nota: {msg.note} | Velocidade: {msg.velocity}")
                        
                        # salva no CSV
                        writer.writerow([timestamp, msg.type, msg.note, msg.velocity])
                        f.flush()  # garante salvar mesmo durante execução
                        
                time.sleep(0.01)
                
        except KeyboardInterrupt:
            print("\nCaptura finalizada.")
