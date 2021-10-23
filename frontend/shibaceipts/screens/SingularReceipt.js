import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { Stack } from 'native-base';

export default function SingularReceipt({ route }) {
    const { text } = route.params;
    return (
        <View>
            <Text>{text}</Text>
        </View>
    )
} 