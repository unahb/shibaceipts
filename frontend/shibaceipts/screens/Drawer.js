import React from 'react'
import { DrawerContentScrollView, DrawerItemList } from '@react-navigation/drawer'
import { View } from 'react-native'
import { Image, Text } from 'react-native-elements'

import { MockCurrentUser } from '../mock_backend'

export default function CustomDrawerContent(props) {
   const { state, ...rest } = props
   const newState = { ...state }
   newState.routes = newState.routes.filter((item) => item.name !== 'Placeholder')
  return (
    <View>
      <Image
        source={{ uri: MockCurrentUser.avatar }}
        style={{
          width: 75,
          height: 75,
          borderRadius: '50%',
          marginTop: 50,
          marginLeft: 20,
          marginBottom: 10,
        }}
      />
      <Text style={{ fontSize: 30, marginLeft: 20, marginBottom: 5 }}>{MockCurrentUser.username}</Text>
      <Text
        style={{
          fontSize: 15,
          marginLeft: 20,
          marginBottom: 10,
          color: 'gray',
        }}
      >
        Current Shibaceipts: {MockCurrentUser.shibaceipts_count}
      </Text>
      <DrawerContentScrollView {...props}>
        <DrawerItemList state={newState} {...rest} />
      </DrawerContentScrollView>
    </View>
  )
}
