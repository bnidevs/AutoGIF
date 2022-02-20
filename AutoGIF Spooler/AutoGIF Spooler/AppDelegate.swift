//
//  AppDelegate.swift
//  AutoGIF Spooler
//
//  Created by Bill Ni on 2/12/22.
//

import Foundation
import Cocoa
import SwiftUI

class AppData: ObservableObject {
    @Published var recorder: Recorder = Recorder.init()
}

class AppDelegate: NSObject, NSApplicationDelegate {
    
    var statusBar: StatusBarController?
    var popover = NSPopover.init()
    
//    @ObservedObject var appdata: AppData = AppData.init()

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        let contentView = ContentView()
        popover.contentViewController = NSHostingController(rootView: contentView)
        statusBar = StatusBarController.init(popover)
    }

    func applicationWillTerminate(_ aNotification: Notification) {
        // Insert code here to tear down your application
    }
}
