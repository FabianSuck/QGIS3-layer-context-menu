def context_menu_metadata():
    print('Ein zusätzlicher Eintrag')
    
customAction = QAction('Metadaten anzeigen')
customAction.triggered.connect(context_menu_metadata)
iface.addCustomActionForLayerType(customAction,'',qgis.core.QgsMapLayerType(0),True)
