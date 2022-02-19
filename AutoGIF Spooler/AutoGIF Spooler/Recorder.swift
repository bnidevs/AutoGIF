//
//  Functionals.swift
//  AutoGIF Spooler
//
//  Created by Bill Ni on 2/12/22.
//

import Foundation
import Aperture

class Recorder {
    public var fileType: Bool = false
    // false == WEBM, true == GIF
    public var recorder: Aperture!
    
    init() {
        let paths = FileManager.default.urls(for: .moviesDirectory, in: .userDomainMask)
        do{
            try recorder = Aperture.init(destination: paths[0])
        }catch{
            print("error oof")
        }
    }

    func startStop(){
        if(recorder!.isRecording){
            recorder!.stop()
        }else{
            recorder!.start()
        }
    }

    func changeFileType(){
        fileType = !fileType;
    }
}
