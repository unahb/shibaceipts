import React from 'react'
import { FlatList, View, TouchableOpacity, StyleSheet } from 'react-native'
import { Card, Button, Icon, Text, Image, FAB } from 'react-native-elements'
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
  return (
    <View>
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
      >
        <Icon name='camera' type='material' size={30} color='#01a699' />
      </TouchableOpacity>
      <FlatList data={MockPosts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item)} />
    </View>
  )
}
