import React from 'react'
import { FlatList, View } from 'react-native'
import { Card, Button, Icon, Text, Image } from 'react-native-elements'
import { MockPosts } from '../mock_backend'

const renderItem = (item) => {
  return (
    <Card>
      <View>
        <Card.Title style={{ textAlign: 'left' }}>
          <View style={{ flexDirection: 'row', alignItems: 'center' }}>
            <Image resizeMode='cover' source={{ uri: item.user.avatar }} style={{ width: 50, height: 50, borderRadius: '50%', marginRight: '15px' }} />
            <Text>{item.user.username}</Text>{' '}
          </View>
        </Card.Title>
        <View style={{ alignItems: 'center' }}>
        <Card.Image source={{ uri: item.shibaceipt }} style={{ width: 300, height: 300 }}></Card.Image>
        </View>
      </View>
    </Card>
  )
}

export default function Home() {
  return <FlatList data={MockPosts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item)} />
}
