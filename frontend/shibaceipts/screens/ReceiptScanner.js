import React, { useState, useEffect, useRef } from 'react'
import { Text, View, TouchableOpacity } from 'react-native'
import { Icon } from 'react-native-elements'
import { Camera } from 'expo-camera'
import * as ImagePicker from 'expo-image-picker'

import { MockCurrentUser } from '../mock_backend'
import { MOCKDATA, APILOCATION } from '../constants'

export default function ReceiptScanner() {
  const [hasPermission, setHasPermission] = useState(null)
  const [cameraRef, setCameraRef] = useState(null)
  const [type, setType] = useState(Camera.Constants.Type.back)
  const [user, setUser] = useState({})

  useEffect(() => {
    if (MOCKDATA) setUser(MockCurrentUser)
    else {
      fetch(`${APILOCATION}get-current-user`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((json) => setUser(json))
    }
  }, [])

  useEffect(() => {
    ;(async () => {
      const { status } = await Camera.requestCameraPermissionsAsync()
      setHasPermission(status === 'granted')
    })()
  }, [])
  if (hasPermission === null) {
    return <View />
  }
  if (hasPermission === false) {
    return <Text>No access to camera</Text>
  }

  const pickImage = async () => {
    let result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ImagePicker.MediaTypeOptions.All,
      allowsEditing: true,
      aspect: [4, 3],
      quality: 1,
    })

    console.log(result)

    if (!result.cancelled) {
      setImage(result.uri)
    }
  }

  return (
    <View style={{ flex: 1 }}>
      <Camera
        style={{ flex: 1 }}
        type={type}
        ref={(ref) => {
          setCameraRef(ref)
        }}
      >
        <View
          style={{
            flex: 1,
            backgroundColor: 'transparent',
            justifyContent: 'flex-end',
          }}
        >
          <TouchableOpacity
            style={{
              borderWidth: 1,
              zIndex: 10,
              borderColor: 'rgba(0,0,0,0.2)',
              alignItems: 'center',
              justifyContent: 'center',
              width: 70,
              position: 'absolute',
              bottom: 10,
              right: 10,
              height: 70,
              backgroundColor: '#fff',
              borderRadius: 100,
            }}
            onPress={async () => {
              let photo = await ImagePicker.launchImageLibraryAsync({
                mediaTypes: ImagePicker.MediaTypeOptions.All,
                allowsEditing: true,
                quality: 1,
              })

              if (!photo.cancelled) {
                console.log('photo', photo)
                var formData = new FormData()
                formData.append('userid', user.username)
                formData.append('receipt', photo.uri)

                fetch(`${APILOCATION}new-receipt`, {
                  method: 'POST',
                  body: formData,
                })
              }
            }}
          >
            <Icon name='image' type='material' size={30} color='#01a699' />
          </TouchableOpacity>
          <TouchableOpacity
            style={{ alignSelf: 'center' }}
            onPress={async () => {
              if (cameraRef) {
                let photo = await cameraRef.takePictureAsync()
                console.log('photo', photo)
                var formData = new FormData()
                formData.append('userid', user.username)
                formData.append('receipt', photo.uri)

                fetch(`${APILOCATION}new-receipt`, {
                  method: 'POST',
                  body: formData,
                })
              }
            }}
          >
            <View
              style={{
                borderWidth: 2,
                borderRadius: '50%',
                borderColor: 'white',
                height: 50,
                width: 50,
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
              }}
            >
              <View
                style={{
                  borderWidth: 2,
                  borderRadius: '50%',
                  borderColor: 'white',
                  height: 40,
                  width: 40,
                  backgroundColor: 'white',
                }}
              ></View>
            </View>
          </TouchableOpacity>
        </View>
      </Camera>
    </View>
  )
}
