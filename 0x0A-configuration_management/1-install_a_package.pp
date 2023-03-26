# puppet script to install puppet-lint

package {'puppet-lint':
  ensure   => 'present',
  provider => 'gem',
}
