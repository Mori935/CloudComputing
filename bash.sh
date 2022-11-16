#!/bin/bash 
az network public-ip create --name myPublicIP --resource-group LabWork_group_10051223
az network nic create -g LabWork_group_10051223 --vnet-name LabWork_group_10051223-vnet --subnet default -n MyNic
az vm create \ 
--name newVM1 \
 --resource-group LabWork_group_10051223 \
 --public-ip-address myPublicIP \
 --public-ip-sku Standard \
 --image MicrosoftWindowsServer:WindowsServer:2019-Datacenter:latest \
 --admin-username C20402034
