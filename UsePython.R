DF = shell('python C:/Stuff/Experiment.py',intern=TRUE)
ColumnNames = unlist(strsplit(gsub("\\[|\\]|'| ","",DF[1]),","))
