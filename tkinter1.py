import tkinter as tk
import pandas as pd
import 
class VehicleManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")

        # Create labels and entries for vehicle information
        self.vehicle_id_label = tk.Label(root, text="Vehicle ID:")
        self.vehicle_id_entry = tk.Entry(root)
        self.vehicle_type_label = tk.Label(root, text="Vehicle Type:")
        self.vehicle_type_entry = tk.Entry(root)
        self.vehicle_color_label = tk.Label(root, text="Vehicle Color:")
        self.vehicle_color_entry = tk.Entry(root)

        # Create buttons for adding and viewing vehicles
        self.add_vehicle_button = tk.Button(root, text="Add Vehicle", command=self.add_vehicle)
        self.view_vehicles_button = tk.Button(root, text="View Vehicles", command=self.view_vehicles)

        # Create a dropdown menu for selecting data to display
        self.display_options = tk.StringVar(root)
        self.display_options.set("All Vehicles")  # default value
        self.display_options_menu = tk.OptionMenu(root, self.display_options, "All Vehicles", "Vehicle IDs", "Vehicle Types", "Vehicle Colors")

        # Layout the widgets
        self.vehicle_id_label.grid(column=0, row=0)
        self.vehicle_id_entry.grid(column=1, row=0)
        self.vehicle_type_label.grid(column=0, row=1)
        self.vehicle_type_entry.grid(column=1, row=1)
        self.vehicle_color_label.grid(column=0, row=2)
        self.vehicle_color_entry.grid(column=1, row=2)
        self.add_vehicle_button.grid(column=0, row=3)
        self.view_vehicles_button.grid(column=1, row=3)
        self.display_options_menu.grid(column=0, row=4)

        # Create a pandas dataframe to store vehicle data
        self.vehicles_df = pd.DataFrame(columns=["Vehicle ID", "Vehicle Type", "Vehicle Color"])

    def add_vehicle(self):
        # Get the vehicle information from the entries
        vehicle_id = self.vehicle_id_entry.get()
        vehicle_type = self.vehicle_type_entry.get()
        vehicle_color = self.vehicle_color_entry.get()

        # Add the vehicle to the dataframe
        self.vehicles_df=[]
        self.vehicles_df.append({"Vehicle ID": vehicle_id, "Vehicle Type": vehicle_type, "Vehicle Color": vehicle_color})

        # Clear the entries
        self.vehicle_id_entry.delete(0, tk.END)
        self.vehicle_type_entry.delete(0, tk.END)
        self.vehicle_color_entry.delete(0, tk.END)

        # Show a success message
        messagebox.showinfo("Success", "Vehicle added successfully!")

    def view_vehicles(self):
        # Get the selected display option
        display_option = self.display_options.get()

        # Create a new window to display the vehicles
        view_window = tk.Toplevel(self.root)
        view_window.title("Vehicles")

        # Create a listbox to display the vehicles
        vehicles_listbox = tk.Listbox(view_window)

        # Display the selected data
        if display_option == "All Vehicles":
            for index, row in self.vehicles_df.iterrows():
                vehicles_listbox.insert(tk.END, f"ID: {row['Vehicle ID']}, Type: {row['Vehicle Type']}, Color: {row['Vehicle Color']}")
        elif display_option == "Vehicle IDs":
            for vehicle_id in self.vehicles_df["Vehicle ID"]:
                vehicles_listbox.insert(tk.END, vehicle_id)
        elif display_option == "Vehicle Types":
            for vehicle_type in self.vehicles_df["Vehicle Type"]:
                vehicles_listbox.insert(tk.END, vehicle_type)
        elif display_option == "Vehicle Colors":
            for vehicle_color in self.vehicles_df["Vehicle Color"]:
                vehicles_listbox.insert(tk.END, vehicle_color)

        # Layout the listbox
        vehicles_listbox.pack()

if __name__ == "__main__":
    import tkinter
    root =tkinter.Tk()
    vehicle_management_system = VehicleManagementSystem(root)
    vehicle_management_system.add_vehicle()
    vehicle_management_system.view_vehicles()
    root.mainloop()
