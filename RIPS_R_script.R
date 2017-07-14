library(MASS)
library(rpart)
library(caret)
library(readr)
xaa_clean <- read_csv("~/Documents/RIP2013/scripts/xaa_clean.csv", 
                      col_types = cols(AmbitosProcedimientoCD = col_integer(), 
                                       Codigo = col_char(), 
                                       CodigoProcedimiento = col_double(), 
                                       CostoConsulta = col_skip(), 
                                       CostoProcedimiento = col_double(), 
                                       DxEgreso = col_skip(), 
                                       DxPrincipal = col_integer(), 
                                       EstadoSalidaDesc = col_skip(), 
                                       FinalidadConsultaCD = col_skip(), 
                                       FinalidadProcedimientosCD = col_double(), 
                                       MunicipioCD = col_character(), 
                                       NetoAPagarConsulta = col_skip(), 
                                       NumeroDiasEstancia = col_skip(), 
                                       PersonaID = col_skip(), 
                                       Prestador = col_double(), 
                                       RegimenAdministradoraDesc = col_integer(), 
                                       SexoDesc =col_factor(c("0","1","2")),
                                       TipoEventoRIPSDesc = col_skip(), 
                                       TipoUsuarioCD = col_integer(), 
                                       fechaid = col_skip()))
xaa<-na.omit(xaa_clean)
xaa<-data.frame(xaa)
set.seed(1) 

xaa.model<-rpart(CodigoProcedimiento ~.,data =xaa,method = "class")
printcp(xaa.model) # display the results 
plotcp(xaa.model) # visualize cross-validation results 
summary(xaa.model) # detailed summary of splits


plot(xaa.model, col="blue", uniform=TRUE,
     main="RIPS Classification Tree")
text(xaa.model, pretty=0, use.n=TRUE, all=TRUE, cex=.8)
post(xaa.model, file = "~/Documents/RIP2013/scripts/RIPStree.ps", 
     title = "RIPS Classification Tree")

