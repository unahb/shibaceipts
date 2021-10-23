import React from 'react'
import { FlatList, View, TouchableOpacity, StyleSheet } from 'react-native'
import { Card, Button, Icon, Text, Image } from 'react-native-elements'
import { MockMySchibaceipts } from '../mock_backend'

const renderItem = (item, navigation) => {
  return (
    <Card>
      <View>
        <View style={{ alignItems: 'center' }}>
          <Card.Image source={{ uri: item.shibaceipt.location }} style={{ width: 300, height: 300 }} onPress={() => navigation.navigate('View Shibaceipt', item.shibaceipt)}></Card.Image>
        </View>
      </View>
    </Card>
  )
}

export default function MyShibaceipts({ navigation }) {
  return (
    <View>
      <FlatList data={MockMySchibaceipts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item, navigation)} />
    </View>
  )
}
