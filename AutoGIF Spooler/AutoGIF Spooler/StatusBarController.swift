//
//  StatusBarController.swift
//  AutoGIF Spooler
//
//  Created by Bill Ni on 2/12/22.
//

import Foundation
import AppKit

class StatusBarController {
    private var statusBar: NSStatusBar
    private var statusItem: NSStatusItem
    private var statusMenu: NSMenu
    
    private var recording: Bool
    
    init() {
        statusBar = NSStatusBar.init()
        statusItem = statusBar.statusItem(withLength: 28.0)
        
        recording = false
        
        statusMenu = NSMenu()
        let startStopButton = NSMenuItem()
        startStopButton.title = recording ? "Stop" : "Start"
        
        statusMenu.addItem(startStopButton)
        
        if let statusBarButton = statusItem.button {
            statusBarButton.image = NSImage(imageLiteralResourceName: "MenuBarIcon")
            statusBarButton.image?.size = NSSize(width: 18.0, height: 18.0)
            statusBarButton.image?.isTemplate = true
            statusBarButton.menu = statusMenu
            statusBarButton.target = self
        }
    }
}
