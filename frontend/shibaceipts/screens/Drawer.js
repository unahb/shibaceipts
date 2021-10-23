import React, { useEffect, useState } from 'react'
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer'
import { View } from 'react-native'
import { Image, Text } from 'react-native-elements'

import { MockCurrentUser } from '../mock_backend'
import { MOCKDATA, APILOCATION } from '../constants'

export default function CustomDrawerContent(props) {
   const { state, ...rest } = props
   const newState = { ...state }
   newState.routes = newState.routes.filter((item) => item.name !== 'Placeholder')

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
  
  return (
    <View>
      <Image
        source={{ uri: user.avatar }}
        style={{
          width: 75,
          height: 75,
          borderRadius: '50%',
          marginTop: 50,
          marginLeft: 20,
          marginBottom: 10,
        }}
      />
      <Text style={{ fontSize: 30, marginLeft: 20, marginBottom: 5 }}>{user.username}</Text>
      <Text
        style={{
          fontSize: 15,
          marginLeft: 20,
          marginBottom: 10,
          color: 'gray',
        }}
      >
        Account Value: {user.account_value}
      </Text>
      <DrawerContentScrollView {...props}>
        <DrawerItemList state={newState} {...rest} />
      </DrawerContentScrollView>
    </View>
  )
}
