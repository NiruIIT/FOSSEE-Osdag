import pandas as pd
import matplotlib.pyplot as plt

def read_excel_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

def plot_diagrams(df):
    if df is None:
        return

    # Create a figure and axis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot Bending Moment Diagram
    ax1.vlines(df['Distance (m)'], 0, df['BM (kN-m)'], color='red', linestyle='dotted')
    ax1.fill_between(df['Distance (m)'], df['BM (kN-m)'], color='red', alpha=0.1)
    ax1.plot(df['Distance (m)'], df['BM (kN-m)'], color='red', marker='o')
    ax1.set_title('Bending Moment Diagram')
    ax1.set_xlabel('Distance (m)')
    ax1.set_ylabel('Bending Moment (kN-m)')
    ax1.grid(True)

    # Annotate maximum and minimum bending moment
    max_bm = df['BM (kN-m)'].max()
    max_bm_pos = df['Distance (m)'][df['BM (kN-m)'].idxmax()]
    min_bm = df['BM (kN-m)'].min()
    min_bm_pos = df['Distance (m)'][df['BM (kN-m)'].idxmin()]

    ax1.annotate(f'Max: {max_bm:.2f} kN-m', xy=(max_bm_pos, max_bm), xytext=(max_bm_pos + 0.1, max_bm + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax1.annotate(f'Min: {min_bm:.2f} kN-m', xy=(min_bm_pos, min_bm), xytext=(min_bm_pos+1 , min_bm),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    # Plot Shear Force Diagram
    ax2.vlines(df['Distance (m)'], 0, df['SF (kN)'], color='blue', linestyle='dotted')
    ax2.fill_between(df['Distance (m)'], df['SF (kN)'], color='blue', alpha=0.1)
    ax2.plot(df['Distance (m)'], df['SF (kN)'], color='blue', marker='o')
    ax2.set_title('Shear Force Diagram')
    ax2.set_xlabel('Distance (m)')
    ax2.set_ylabel('Shear Force (kN)')
    ax2.grid(True)

    # Annotate maximum and minimum shear force
    max_sf = df['SF (kN)'].max()
    max_sf_pos = df['Distance (m)'][df['SF (kN)'].idxmax()]
    min_sf = df['SF (kN)'].min()
    min_sf_pos = df['Distance (m)'][df['SF (kN)'].idxmin()]

    ax2.annotate(f'Max: {max_sf:.2f} kN', xy=(max_sf_pos, max_sf), xytext=(max_sf_pos + 0.1, max_sf + 5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax2.annotate(f'Min: {min_sf:.2f} kN', xy=(min_sf_pos, min_sf), xytext=(min_sf_pos+0.2, min_sf),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

    plt.tight_layout()
    plt.show()

def main():
    # File path to the Excel sheet
    file_path = 'SFS_Screening_SFDBMD.xlsx'
    
    # Read data from Excel
    df = read_excel_data(file_path)
    
    # Plot the diagrams
    plot_diagrams(df)

if __name__ == "__main__":
    main()