import React, { useEffect } from 'react';
import { SafeAreaView, ScrollView, StatusBar, StyleSheet, Text, useColorScheme, View, Alert } from 'react-native';
import messaging from '@react-native-firebase/messaging';
import { Colors, Header } from 'react-native/Libraries/NewAppScreen';

const App = (): React.JSX.Element => {
  const isDarkMode = useColorScheme() === 'dark';

  useEffect(() => {
    // Request permission to receive notifications
    const requestPermission = async () => {
      const authStatus = await messaging().requestPermission();
      const enabled = authStatus === messaging.AuthorizationStatus.AUTHORIZED || authStatus === messaging.AuthorizationStatus.PROVISIONAL;
      if (enabled) {
        console.log('Authorization status:', authStatus);
      }
    };

    requestPermission();

    // Foreground message listener
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      Alert.alert('A new FCM message arrived!', JSON.stringify(remoteMessage));
    });

    return unsubscribe;
  }, []);

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar barStyle={isDarkMode ? 'light-content' : 'dark-content'} backgroundColor={backgroundStyle.backgroundColor} />
      <ScrollView contentInsetAdjustmentBehavior="automatic" style={backgroundStyle}>
        <Header />
        <View style={{ backgroundColor: isDarkMode ? Colors.black : Colors.white }}>
          <Text style={styles.sectionTitle}>Firebase Cloud Messaging Setup</Text>
          <Text style={styles.sectionDescription}>Ready to receive push notifications!</Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
    padding: 16,
  },
  sectionDescription: {
    fontSize: 18,
    fontWeight: '400',
    padding: 16,
  },
});

export default App;
