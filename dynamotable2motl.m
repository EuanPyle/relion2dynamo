table_name=input('Input dynamo table file name to be converted to motl: ','s'); %relion2dynamo output .tbl

output_dir=input('Output new directory name: ','s'); 

table=dread(table_name);

%Adapt make_motl to output a motl file for each tomogram in a folder called RELION_motl

tomolist=unique(table(:,20));

for i=1:length(tomolist)
    tomon=tomolist(i);
    motl_table=table(table(:,20)==tomon,:);
    motl_table=dynamo__table2motl(motl_table);
    dwrite(motl_table,['./' output_dir '/RELION_motl_TS_' num2str(tomon) '.em']); 
end

disp(['Writing motl files into ' output_dir]);


