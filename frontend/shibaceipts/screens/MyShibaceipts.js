import React, { useEffect, useState } from 'react'
import { FlatList, View, TouchableOpacity, StyleSheet } from 'react-native'
import { Card, Button, Icon, Text, Image } from 'react-native-elements'
import { MockMySchibaceipts } from '../mock_backend'
import { MOCKDATA, APILOCATION } from '../constants'

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
  const [shibaceipts, setShibaceipts] = useState([])

  useEffect(() => {
    if (MOCKDATA) setShibaceipts(MockPosts)
    else {
      fetch(`${APILOCATION}get-current-user-shibaceipts`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((json) => setShibaceipts(json.data))
    }
  }, [])
  return (
    <View>
      <FlatList data={shibaceipts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item, navigation)} />
    </View>
  )
}
