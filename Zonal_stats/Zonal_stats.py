import os,glob
in_files = glob.glob('C:/Users/Task/8bit-convert/3hour/*.tif')
input_vector = '"C:/Users/Task/Aluva_building/aluva_buildings_UUID.shp"'
output_csv_dir = '"C:/Users/Task/Output"'

for in_file in in_files: 
      f_name = os.path.basename(in_file)[6:25]
      output_csv = output_csv_dir+'/'+f_name+'.csv'

      if not os.path.exists(output_csv):             
            # statistics = '[2,3]'
            command = (
            f"qgis_process run native:zonalstatisticsfb "
            f"--INPUT={input_vector} "
            f"--INPUT_RASTER={in_file} "
            f"--RASTER_BAND=1 "
            f"--COLUMN_PREFIX=_ "
            f"--STATISTICS=6 "
            f"--OUTPUT={output_csv}")
            
            os.system(command)

