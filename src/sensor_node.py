import os
import csv
import json
import random
from datetime import datetime

class SensorNode:
    """Represents a base atmospheric sensor node monitoring tactical environments."""
    
    def __init__(self, node_id: str, threshold_idlh: float) -> None:
        """Initializes base parameters. Precondition: threshold_idlh > 0."""
        self.node_id: str = node_id
        self.threshold_idlh: float = threshold_idlh

    def validate_reading(self, value: float) -> str:
        """Enforces invariant logical validation contracts over telemetry metrics."""
        if value < 0.0:
            return "MALFUNCTION"
        return "CRITICAL" if value >= self.threshold_idlh else "CLEAR"


class ChemicalSensorNode(SensorNode):
    """Specialized node for tracking hazardous chemical agents."""
    
    def __init__(self, node_id: str, agent_name: str, threshold_idlh: float) -> None:
        super().__init__(node_id, threshold_idlh)
        self.agent_name: str = agent_name
        
    def generate_reading(self) -> dict:
        """Generates chemical concentration payload profiles using fractional PPM metrics."""
        # Intentionally inject occasional hardware fault (-1.0) to test downstream code robustness
        if random.random() > 0.98:
            raw_ppm = -1.0
        else:
            raw_ppm = round(random.uniform(0.02, 3.5), 3)
            if random.random() > 0.92:  # Simulated contamination release spike
                raw_ppm = round(raw_ppm + random.uniform(15.0, 50.0), 3)
                
        status = self.validate_reading(raw_ppm)
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "metric_type": "Chemical",
            "agent": self.agent_name,
            "value": raw_ppm,
            "status": status
        }


class WeatherNode(SensorNode):
    """Tracks localized weather attributes necessary for downstream plume propagation math."""
    
    def __init__(self, node_id: str) -> None:
        # Weather stations don't use simple IDLH thresholds, set arbitrary base
        super().__init__(node_id, threshold_idlh=999.0)
        
    def generate_reading(self) -> dict:
        """Captures vector-based environmental telemetry values."""
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "metric_type": "Meteorological",
            "wind_speed_ms": round(random.uniform(0.5, 12.5), 1),
            "wind_direction_deg": random.randint(0, 359),
            "temperature_c": round(random.uniform(15.0, 28.5), 1)
        }


def log_telemetry_to_csv(filepath: str, payload: dict) -> None:
    """Appends structural telemetry dictionaries cleanly into flat disk files.
    
    Preconditions:
        - payload must be a flat dictionary structure.
        - filepath must target a valid operational location.
    Postconditions:
        - Creates destination directory dynamically if not present.
        - Synchronizes internal code state with external physical storage safely.
    """
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
        
    file_exists = os.path.isfile(filepath)
    with open(filepath, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=payload.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(payload)


if __name__ == "__main__":
    # Initialize our heterogeneous network elements
    gas_detector = ChemicalSensorNode("CHEM-ALPHA-01", "Sarin", 0.05)
    met_station = WeatherNode("MET-METEO-01")
    
    csv_target_path = "data/raw/telemetry_stream.csv"
    
    print("--- Executing Multi-Node Operational Array Generation ---")
    for _ in range(3):
        chem_data = gas_detector.generate_reading()
        weather_data = met_station.generate_reading()
        
        # Log records out to disk
        log_telemetry_to_csv(csv_target_path, chem_data)
        print(f"Logged {chem_data['metric_type']} -> Status: {chem_data['status']} | Value: {chem_data['value']}")
