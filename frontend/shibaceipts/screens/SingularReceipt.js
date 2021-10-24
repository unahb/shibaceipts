import React from 'react'
import { View } from 'react-native'
import { Image, Text, Card, Button, Icon } from 'react-native-elements'

import { APILOCATION } from '../constants'

export default function SingularReceipt({ route }) {
  console.log(route)
  return (
    <View style={{ alignItems: 'center' }}>
      <Image source={{ uri: `${APILOCATION}${route.params.location}` }} style={{ width: 300, height: 300 }} />
    </View>
  )
}
