import os
import random
import time
from datetime import datetime

class SensorNode:
    """Represents a localized CBRN atmospheric sensor node monitoring dangerous gases.

    Attributes:
        node_id (str): A unique alphanumeric identifier for the physical sensor placement.
        gas_type (str): The specific chemical, biological, or radiological agent monitored.
        threshold_idlh (float): Immediately Dangerous to Life or Health limit in parts per million (PPM).
    """
    
    def __init__(self, node_id: str, gas_type: str, threshold_idlh: float) -> None:
        """Initializes the sensor node with tracking configurations.

        Preconditions:
            - node_id must be a non-empty string.
            - threshold_idlh must be a positive float or integer (> 0.0).

        Postconditions:
            - Instantiates a SensorNode instance with localized immutable state attributes.
        """
        self.node_id: str = node_id
        self.gas_type: str = gas_type
        self.threshold_idlh: float = threshold_idlh
        
    def generate_reading(self) -> dict:
        """Simulates an atmospheric air intake sample with seasonal baseline drift.

        Preconditions:
            - The SensorNode object must be initialized with valid hardware telemetry parameters.

        Postconditions:
            - Returns a dictionary containing structural keys: 'timestamp', 'node_id', 
              'agent', 'concentration_ppm', and 'status'.
            - The value of 'concentration_ppm' is returned as a rounded float to 3 decimal places.
            - Evaluates 'status' strictly as 'CRITICAL' if 'concentration_ppm' matches or exceeds 
              the 'threshold_idlh' boundary, otherwise returns 'CLEAR'.
              
        Returns:
            dict: An operational data payload snapshot mapping live environmental telemetries.
        """
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