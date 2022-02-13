//
//  AutoGIFApp.swift
//  AutoGIF Spooler
//
//  Created by Bill Ni on 2/12/22.
//

import Foundation
import SwiftUI

@main struct AutoGIFApp: App {
    
    @NSApplicationDelegateAdaptor var delegate: AppDelegate
    
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
    
    init() { }
    
}
