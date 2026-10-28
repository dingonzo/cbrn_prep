import os
import random
import time
from datetime import datetime

class SensorNode:
    """Represents a localized CBRN atmospheric sensor node monitoring dangerous gases."""
    
    def __init__(self, node_id: str, gas_type: str, threshold_idlh: float):
        self.node_id = node_id
        self.gas_type = gas_type
        self.threshold_idlh = threshold_idlh  # Immediately Dangerous to Life or Health limit
        
    def generate_reading(self) -> dict:
        """Simulates an atmospheric air intake sample with seasonal baseline drift."""
        # Baseline clean air reading with random sensor noise spikes
        base_ppm = random.uniform(0.1, 4.5)
        
        # Simulate a 10% chance of a toxic localized release incident
        if random.random() > 0.90:
            base_ppm += random.uniform(25.0, 75.0)
            
        reading_val = round(base_ppm, 3)
        status = "CRITICAL" if reading_val >= self.threshold_idlh else "CLEAR"
        
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "agent": self.gas_type,
            "concentration_ppm": reading_val,
            "status": status
        }

if __name__ == "__main__":
    # Initialize a sensor node watching for Chlorine Gas (IDLH threshold: 10.0 ppm)
    chlorine_sensor = SensorNode(node_id="NODE-ALPHA-01", gas_type="Chlorine", threshold_idlh=10.0)
    
    print(f"--- Launching CBRN Sensor Tracking Lifecycle [{chlorine_sensor.node_id}] ---")
    
    # Generate 5 consecutive telemetry readouts to verify terminal logic
    for _ in range(5):
        telemetry = chlorine_sensor.generate_reading()
        print(f"[{telemetry['timestamp']}] {telemetry['agent']}: {telemetry['concentration_ppm']} PPM | Status: {telemetry['status']}")
        time.sleep(1)
import os
import random
import time
from datetime import datetime

class SensorNode:
    """Represents a localized CBRN atmospheric sensor node monitoring dangerous gases."""
    
    def __init__(self, node_id: str, gas_type: str, threshold_idlh: float):
        self.node_id = node_id
        self.gas_type = gas_type
        self.threshold_idlh = threshold_idlh  # Immediately Dangerous to Life or Health limit
        
    def generate_reading(self) -> dict:
        """Simulates an atmospheric air intake sample with seasonal baseline drift."""
        # Baseline clean air reading with random sensor noise spikes
        base_ppm = random.uniform(0.1, 4.5)
        
        # Simulate a 10% chance of a toxic localized release incident
        if random.random() > 0.90:
            base_ppm += random.uniform(25.0, 75.0)
            
        reading_val = round(base_ppm, 3)
        status = "CRITICAL" if reading_val >= self.threshold_idlh else "CLEAR"
        
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_id,
            "agent": self.gas_type,
            "concentration_ppm": reading_val,
            "status": status
        }

if __name__ == "__main__":
    # Initialize a sensor node watching for Chlorine Gas (IDLH threshold: 10.0 ppm)
    chlorine_sensor = SensorNode(node_id="NODE-ALPHA-01", gas_type="Chlorine", threshold_idlh=10.0)
    
    print(f"--- Launching CBRN Sensor Tracking Lifecycle [{chlorine_sensor.node_id}] ---")
    
    # Generate 5 consecutive telemetry readouts to verify terminal logic
    for _ in range(5):
        telemetry = chlorine_sensor.generate_reading()
        print(f"[{telemetry['timestamp']}] {telemetry['agent']}: {telemetry['concentration_ppm']} PPM | Status: {telemetry['status']}")
        time.sleep(1)

