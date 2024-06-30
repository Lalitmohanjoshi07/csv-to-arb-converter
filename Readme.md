This is a python script to convert any translations csv file into arb file
this is to reduce the time and effort of the developers on localization files

here are steps how to use it(first ensure your system has python installed)
first take clone of this repo on your system
1. Prepare Your Excel Sheet:

      Ensure your Excel sheet has columns for the keys and each language. For example:

          Key | English | Hungarian | Spanish | German | French

      Ensure that there should be the first row that tells the locale of each language with key '@@locale'. For example

         Key      | English | Hungarian | Spanish | German | French

         @@locale | en      | hu        | es      | de     | fr

      Each row should correspond to a different string.

      No need to add the metadata for any string

   
2.Save the Excel Sheet as CSV:

    Save the Excel sheet as a CSV file. This can be done through 'File > Save As > .CSV'.

    Ensure your file is saved with name translations.csv on the root directory of this repo
    
    
3.Use the given Script to Convert CSV to ARB

4. It will generate your arb translations file and save them in the root folder of this repo


(Note: if you are a python developer feel free to modify script based on your preferrence)
