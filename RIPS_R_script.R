#Script for develop feature models by dataminig techniques 
#josepplloo
#Maestria en ingenieria
#universidad de antioquia
#2017
#Fuente:
#James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).
#An introduction to statistical learning (Vol. 112). New York: springer.
#este script usa las variables en los RIPS considerando DxPrincipal:
#RegimenAdministradoraDesc,FinalidadProcedimientosCD,
#TipoUsuarioCD,AmbitosProcedimientoCD,Edad,SexoDesc
#para predecir CodigoProcedimiento
# las variables son 
#1-RegimenAdministradoraDesc: id del regimen: Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
#2-DxPrincipal: diagnostico principal
#3-FinalidadProcedimientosCD: si la finalidad es diagnostica-terapeutica
#4-TipoUsuarioCD: si el usuario es Contributivo-Subsidiado-Vinculado-Particular-Otro-Desplazado
#5-AmbitosProcedimientoCD: si es ambulatorio(2)-hospitalario(0)-urgencias(1)
#6-CodigoProcedimiento: procedimiento medico
#7-Edad: edad
#8-SexoDesc: genero del usuario

# la idea de este ejercicio es mostrar el comportamineto de diferentes modelos y exportar a pmml
#leo el archivo

library(readr)
xaa_0 <- read_csv("~/Documents/scripts/RIPS_2013_1/splitDx/1219.csv", 
                      col_types = cols(
                        DxPrincipal=col_skip(),
                        RegimenAdministradoraDesc=col_factor(c("3", "2")),
                        FinalidadProcedimientosCD=col_factor(c("1","2")),
                        TipoUsuarioCD=col_factor(c("2","1")),
                        AmbitosProcedimientoCD=col_factor(c("2","0","1")),
                        CodigoProcedimiento=col_factor(c("123",
                                                         "1434",
                                                         "1435",
                                                         "1458",
                                                         "1671",
                                                         "1678",
                                                         "1695",
                                                         "1775",
                                                         "1902",
                                                         "1924",
                                                         "2137",
                                                         "2343",
                                                         "2622",
                                                         "2772",
                                                         "2775",
                                                         "2776",
                                                         "2795",
                                                         "2796",
                                                         "2797",
                                                         "2798",
                                                         "2801",
                                                         "2803",
                                                         "2811",
                                                         "2824")),
                        Edad=col_integer(),
                        SexoDesc=col_factor(c("2","0","1","3"))))
xaa<-na.omit(xaa_0)
xaa<-data.frame(xaa)
 
#Arboles de clasificacion
set.seed(2)
traintest <-sample (1: nrow(xaa), 0.7*nrow(xaa))
xaa.train <-xaa[traintest,]
xaa.test <- xaa[-traintest,]
library(rpart)
tree.model <-rpart(CodigoProcedimiento ~., data=xaa.train)
print("###Tree###")
plot(tree.model)
text(tree.model)
title("Training Set's Classification Tree")
print(tree.model)
print("###Summary###")
print(summary(tree.model))
print("###prediction###")
tree.pred<-predict(tree.model,xaa.test,type="class")
print(table(xaa.test$CodigoProcedimiento,tree.pred))
print("###prune tree###")
tree.prune<-prune(tree.model, cp=0.02)
print(summary(tree.prune))
plot(tree.prune)
text(tree.prune)
title("Training Set's Classification Prune Tree")
library(partykit)
tree.rparty<-as.party(tree.prune)
print("###prune tree partykit###")
print(summary(tree.rparty))
plot(tree.rparty)
print("###random forest###")
library("randomForest")
rf<-randomForest(CodigoProcedimiento~.,data=xaa,
                  do.trace=100, ntree=100)
print(rf)
library(pmml)
tree.xml<-pmml(rf)
saveXML(tree.xml,file="~/Documents/scripts/RIPStreeDx1219.xml")
