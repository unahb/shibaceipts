import React, { useEffect, useState } from 'react'
import { FlatList, View, TouchableOpacity, StyleSheet } from 'react-native'
import { Card, Button, Icon, Text, Image, FAB } from 'react-native-elements'
import { useIsFocused } from '@react-navigation/native'
import Countdown from 'react-countdown'

import { MockPosts } from '../mock_backend'
import { MOCKDATA, APILOCATION } from '../constants'

const renderItem = (item, navigation) => {
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
          <Card.Image source={{ uri: item.shibaceipt.location }} style={{ width: 300, height: 300 }} onPress={() => navigation.navigate('View Shibaceipt', item.shibaceipt)}></Card.Image>
        </View>
        <View style={{ display: 'flex', justifyContent: 'space-between', flexDirection: 'row', marginTop: '10px' }}>
          <Text style={{ fontSize: 15 }}>Price: {item.shibaceipt.value}Ð</Text>
          <Text style={{ fontSize: 15 }}>⏳ <Countdown date={item.shibaceipt.expiration} /></Text>
        </View>
      </View>
    </Card>
  )
}

export default function Home({ navigation }) {
  //console.log(JSON.stringify(MockPosts))
  const [posts, setPosts] = useState([])
  
    const isFocused = useIsFocused()

    useEffect(() => {
      if (MOCKDATA) setPosts(MockPosts)
      else {
        fetch(`${APILOCATION}get-shibaceipts`, {
          method: 'GET',
        })
          .then((response) => response.json())
          .then((json) => setPosts(json.data))
      }
    }, [isFocused])

  useEffect(() => {
    if (MOCKDATA) setPosts(MockPosts)
    else {
      fetch(`${APILOCATION}get-shibaceipts`, {
        method: 'GET',
      })
        .then((response) => response.json())
        .then((json) => setPosts(json.data))
    }
  }, [])

  return (
    <View>
      {/*
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
      */}
      <FlatList data={posts} keyExtractor={(item) => item.shibaceipt} renderItem={({ item }) => renderItem(item, navigation)} />
    </View>
  )
}
