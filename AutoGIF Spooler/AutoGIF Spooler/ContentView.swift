//
//  ContentView.swift
//  AutoGIF Spooler
//
//  Created by Bill Ni on 2/12/22.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        Button(action: startStop) {
            Text("Test")
        }.frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}


struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
